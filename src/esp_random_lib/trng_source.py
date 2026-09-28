import serial
import time
from .exceptions import DeviceConnectionError, DataReadError


class ESP32Random:
    def __init__(self, port: str, baudrate: int = 115200, timeout: float = 2.0):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self._serial = None

        self._connect()

    def __del__(self):
        try:
            self.close()
        except Exception:
            pass

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

    def close(self):
        if self._serial is not None and self._serial.is_open:
            self._serial.close()
            self._serial = None

    def get_random_bytes(self, count: int) -> bytes:
        if self._serial is None or not self._serial.is_open:
            raise DeviceConnectionError("Serial port is closed, unable to get random bytes")

        try:
            data = self._serial.read(count)
        except serial.SerialException as e:
            self.close()
            raise DeviceConnectionError("Lost connection with device during reading data")

        if len(data) < count:
            raise DataReadError(f"Timeout error during reading data, wanted {count} bytes, got {len(data)}")
        return data
