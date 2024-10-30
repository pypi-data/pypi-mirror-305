from .serial_device import SerialDevice

class Arduino(SerialDevice):
    """Arduino device class with predefined PID/VIDs."""
    PIDVIDS = ['2341:0043', '2341:0010', '0403:6001']

    def __init__(self, port=None, baudrate=9600, timeout=2, read_size=1, data_handler=None):
        super().__init__(pidvid=self.PIDVIDS, port=port, baudrate=baudrate,
                         timeout=timeout, read_size=read_size, data_handler=data_handler)

class Pico(SerialDevice):
    """Raspberry Pi Pico device class with predefined PID/VIDs."""
    PIDVIDS = ['2E8A:0005']

    def __init__(self, port=None, baudrate=9600, timeout=2, read_size=1, data_handler=None):
        super().__init__(pidvid=self.PIDVIDS, port=port, baudrate=baudrate,
                         timeout=timeout, read_size=read_size, data_handler=data_handler)

class Teensy(SerialDevice):
    """Teensy device class with predefined PID/VIDs."""
    PIDVIDS = ['16C0:0483', '16C0:0487']

    def __init__(self, port=None, baudrate=9600, timeout=2, read_size=1, data_handler=None):
        super().__init__(pidvid=self.PIDVIDS, port=port, baudrate=baudrate,
                         timeout=timeout, read_size=read_size, data_handler=data_handler)
