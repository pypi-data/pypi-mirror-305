import serial.tools.list_ports
import logging

logger = logging.getLogger(__name__)

def detect_ports(pidvid_list=None):
    """Detect available serial ports based on PID/VIDs."""
    matched_ports = []
    for port in serial.tools.list_ports.comports():
        if pidvid_list and any(pidvid in port.hwid for pidvid in pidvid_list):
            logger.info(f"Found device at {port.device}")
            matched_ports.append(port.device)
    return matched_ports