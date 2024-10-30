import json
from .serial_device import SerialDevice

# Path to the device configuration JSON
CONFIG_FILE = "devices.json"

def load_device_classes(json_file=CONFIG_FILE):
    """Dynamically generate device classes from a JSON configuration file."""
    with open(json_file, "r") as f:
        devices = json.load(f)

    device_classes = {}
    for device in devices:
        class_name = device["name"]
        cls = create_device_class(
            class_name,
            device["pidvids"],
            device.get("default_baudrate", 9600),
            device.get("default_timeout", 2)
        )
        device_classes[class_name] = cls

    return device_classes

def create_device_class(name, pidvids, default_baudrate, default_timeout):
    """Create a device class dynamically."""
    cls = type(
        name,
        (SerialDevice,),
        {
            "PIDVIDS": pidvids,
            "__init__": create_init(default_baudrate, default_timeout)
        }
    )
    return cls

def create_init(default_baudrate, default_timeout):
    """Create the __init__ method dynamically for each class."""
    def __init__(self, port=None, baudrate=None, timeout=None, read_size=1, data_handler=None):
        baudrate = baudrate or default_baudrate
        timeout = timeout or default_timeout

        # Initialize the parent class
        super(self.__class__, self).__init__(
            pidvid=self.PIDVIDS,
            port=port,
            baudrate=baudrate,
            timeout=timeout,
            read_size=read_size,
            data_handler=data_handler
        )
    return __init__

def register_device(name, pidvids, default_baudrate=9600, default_timeout=2):
    """Register a new device class dynamically."""
    cls = create_device_class(name, pidvids, default_baudrate, default_timeout)
    globals()[name] = cls  # Make the class available globally
    return cls

# Load device classes from the JSON configuration and register them
device_classes = load_device_classes()
globals().update(device_classes)
