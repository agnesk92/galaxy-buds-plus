import logging

import bluetooth

from logger import config_logger

config_logger()
logger = logging.getLogger(__name__)

UUID = "00001101-0000-1000-8000-00805F9B34FB"


def parse_battery_info(sock):
    data = sock.recv(1024)

    batterylife = None
    logger.info(f"Data 3rd elem: {data[3]}")
    if data[3] in [96, 97]:
        if data[3] == 97:
            batterylife = (data[6], data[7], data[11])
        elif data[3] == 96:
            batterylife = (data[5], data[6], data[10])

    while data[3] not in [96, 97] and len(data) != 0:
        logger.info(f"Data battery elem: {data[3]}")
        logger.info(f"Data length: {len(data)}")
        data = sock.recv(1024)
        if data[3] == 97:
            batterylife = (data[6], data[7], data[11])
        elif data[3] == 96:
            batterylife = (data[5], data[6], data[10])

    if batterylife is None:
        raise Exception("Couldn't get battery info")

    logger.info(f"Battery life set: {batterylife}")
    return batterylife


def get_battery_levels(bltooth_address):
    service_matches = bluetooth.find_service(uuid=UUID, address=bltooth_address)
    host = service_matches[0]["host"]
    port = service_matches[0]["port"]

    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((host, port))

    batterylife = parse_battery_info(sock)
    return batterylife


if __name__ == "__main__":
    get_battery_levels("34:82:C5:31:5D:B1")
