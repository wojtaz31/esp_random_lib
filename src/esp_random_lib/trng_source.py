import serial
import time
from .exceptions import DeviceConnectionError


class ESP32Random:
    def __init__(self, port: str, baudrate: int = 115200, timeout: float = 2.0):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self._serial = None

        self._connect()

    def _connect(self) -> None:
        try:
            self._serial = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout
            )

            time.sleep(1.5)
            self._serial.reset_input_buffer()

        except serial.SerialException as e:
            raise DeviceConnectionError(f"Nie udało połączyć się z ESP na portcie {self.port}. {e}")