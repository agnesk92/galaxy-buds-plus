import logging

import bluetooth

from logger import config_logger

config_logger()
logger = logging.getLogger(__name__)

UUID = "00001101-0000-1000-8000-00805F9B34FB"


def parse_battery_info(data):
    batterylife = None
    while data[3] not in [96, 97] and len(data) != 0:
        logger.info(f"Data battery elem: {data[3]}")

        data = sock.recv(1024)
        logger.info(len(data))
        if data[3] == 97:
            batterylife = (data[6], data[7], data[11])
        if data[3] == 96:
            batterylife = (data[5], data[6], data[10])

    if batterylife is None:
        raise Exception("Couldn't get battery info")

    return batterylife


def get_battery_levels(bltooth_address):
    service_matches = bluetooth.find_service(uuid=UUID, address=bltooth_address)
    host = service_matches[0]["host"]
    port = service_matches[0]["port"]

    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((host, port))

    data = sock.recv(1024)
    batterylife = parse_battery_info(data)
    return batterylife
