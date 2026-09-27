class ESPRandomError(Exception):
    """Bazowa klasa wyjątków dla biblioteki esp_random_lib"""
    pass

class DeviceConnectionError(ESPRandomError):
    """Wyjątek rzucany, w przypadku błędu połączenia z ESP32"""
    pass