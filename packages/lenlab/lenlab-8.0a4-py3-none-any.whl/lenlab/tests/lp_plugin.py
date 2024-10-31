from collections.abc import Generator
from contextlib import closing
from dataclasses import dataclass
from logging import getLogger
from typing import Self

import pytest
from PySide6.QtCore import QIODeviceBase
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo

from lenlab.bsl import BootstrapLoader
from lenlab.launchpad import find_launchpad
from lenlab.protocol import Protocol

logger = getLogger(__name__)


def pytest_addoption(parser):
    # pytest_addoption requires a plugin
    # pytest imports conftest within a package only after cli parsing
    parser.addoption(
        "--port",
        action="store",
        help="launchpad serial port name",
    )
    parser.addoption(
        "--fw",
        action="store_true",
        default=False,
        help="assume launchpad with firmware",
    )
    parser.addoption(
        "--bsl",
        action="store_true",
        default=False,
        help="assume launchpad with BSL",
    )
    parser.addoption(
        "--flash",
        action="store_true",
        default=False,
        help="allow to flash the firmware",
    )


phase_report_key = pytest.StashKey[dict[str, pytest.CollectReport]]()


@pytest.hookimpl(wrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    rep = yield

    # store test results for each phase of a call, which can
    # be "setup", "call", "teardown"
    item.stash.setdefault(phase_report_key, {})[rep.when] = rep

    return rep


@pytest.fixture(scope="session")
def port_infos() -> list[QSerialPortInfo]:
    return QSerialPortInfo.availablePorts()


class LaunchpadError(Exception):
    pass


@dataclass(slots=True, frozen=True)
class Launchpad:
    port_info: QSerialPortInfo
    firmware: bool = False
    bsl: bool = False
    flash: bool = False

    firmware_baudrate = 1_000_000
    default_baudrate = 9_600

    # shortcuts
    knock_packet = Protocol.knock_packet
    connect_packet = BootstrapLoader.connect_packet
    ok_packet = BootstrapLoader.ok_packet

    @property
    def baud_rate(self) -> int:
        return self.firmware_baudrate if self.firmware else self.default_baudrate

    @property
    def port_name(self) -> str:
        return self.port_info.portName()

    def open_port(self) -> QSerialPort:
        port = QSerialPort(self.port_info)
        if not port.open(QIODeviceBase.OpenModeFlag.ReadWrite):
            raise LaunchpadError(port.errorString())

        port.setBaudRate(self.baud_rate)
        port.clear()  # The OS may have leftovers in the buffers
        return port

    @classmethod
    def discover(cls, port_infos: list[QSerialPortInfo]) -> Generator[Self]:
        for port_info in port_infos:
            launchpad = None
            with closing(cls(port_info).open_port()) as port:
                port.setBaudRate(cls.firmware_baudrate)
                port.write(cls.knock_packet)
                if port.waitForReadyRead(100):
                    reply = port.readAll().data()
                    if reply and cls.knock_packet.startswith(reply):
                        launchpad = cls(QSerialPortInfo(port), firmware=True)
                        logger.info(f"{launchpad.port_name}: firmware found")
                        yield launchpad

                port.setBaudRate(cls.default_baudrate)
                port.write(cls.connect_packet)
                if port.waitForReadyRead(100):
                    reply = port.readAll().data()
                    if reply and cls.ok_packet.startswith(reply):
                        launchpad = cls(QSerialPortInfo(port), bsl=True)
                        logger.info(f"{launchpad.port_name}: BSL found")
                        yield launchpad

            if not launchpad:
                logger.info(f"{port_info.portName()}: nothing found")


@pytest.fixture(scope="session")
def launchpad(request, port_infos: list[QSerialPortInfo]) -> Launchpad:
    if port_name := request.config.getoption("port"):
        matches = [port_info for port_info in port_infos if port_info.portName() == port_name]
    else:
        matches = find_launchpad(port_infos)

    if not matches:
        pytest.skip("no port found")

    _firmware = request.config.getoption("fw")
    _bsl = request.config.getoption("bsl")
    _flash = request.config.getoption("flash")
    if sum([_firmware, _bsl, _flash]) > 1:
        pytest.skip("only one --fw, --bsl, or --flash")

    if _firmware or _bsl or _flash:
        if len(matches) > 1:
            pytest.skip("cannot choose port")

        launchpad = Launchpad(
            matches[0],
            firmware=_firmware,
            bsl=_bsl,
            flash=_flash,
        )
        return launchpad

    launchpad = next(Launchpad.discover(matches), None)
    if not launchpad:
        pytest.skip("no launchpad found")

    return launchpad


@pytest.fixture(scope="session")
def firmware(launchpad: Launchpad) -> Launchpad:
    if launchpad.firmware:
        return launchpad

    pytest.skip("no firmware found")


@pytest.fixture(scope="session")
def bsl(launchpad: Launchpad) -> Launchpad:
    if launchpad.bsl:
        return launchpad

    pytest.skip("no BSL found")


@pytest.fixture(scope="session")
def flash(request, launchpad: Launchpad) -> Launchpad:
    if launchpad.flash:
        return launchpad

    pytest.skip("flash not enabled")


@pytest.fixture(scope="module")
def port(launchpad: Launchpad) -> QSerialPort:
    port = launchpad.open_port()
    yield port
    port.close()


@pytest.fixture
def cleanup(request, port: QSerialPort):
    yield

    report = request.node.stash[phase_report_key]
    if "call" in report and report["call"].failed:
        logger.info("cleanup")
        while port.waitForReadyRead(300):  # wait for timeout
            pass

        if port.bytesAvailable():
            logger.warning("spurious bytes cleaned up")

        port.clear()
