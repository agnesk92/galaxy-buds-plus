import logging

import pydbus

from logger import config_logger

config_logger()
logger = logging.getLogger(__name__)


class DeviceInfo:

    def __init__(self):
        bus = pydbus.SystemBus()
        self.adapter = bus.get('org.bluez', '/org/bluez/hci0')
        self.mngr = bus.get('org.bluez', '/')

    def get_devices(self):
        mngd_objs = self.mngr.GetManagedObjects()
        devices = [mngd_objs[path].get('org.bluez.Device1', {}) for path in mngd_objs]
        return devices

    @property
    def devices(self):
        return self.get_devices()
   
    @property
    def connected_devices(self):
        conn_devices = [el for el in self.devices if el.get('Connected', False)]
        return conn_devices

    def get_similar_device_names(self, name):
        similar_names = [el.get('Name') for el in self.devices if name in el.get('Name', "")]
        # return "Galaxy Buds+ (5DB1)"
        return similar_names

    def get_device_address(self, device_name):
        address = [el.get('Address') for el in self.devices if device_name == el.get("Name", "")]
        if len(address) == 0:
            raise Exception(f"No device called {device_name} found.")

        return address[0]

    def get_device_info(self, name=None, address=None):
        if name is not None:
            device_info = [el for el in self.devices if name == el.get("Name", "")]
        elif address is not None: 
            device_info = [el for el in self.devices if address == el.get("Address", "")]
        else:
            raise Exception("Please specify the address or the name of the device.")
        
        if len(device_info) == 0:
            raise Exception("No device found.")

        return device_info[0]

        
    def is_device_connected(self, name=None, address=None):
        if name is not None:
            is_connected = self.get_device_info(name=name).get("Connected", False)
        elif address is not None:
            is_connected = self.get_device_info(address=address).get("Connected", False)
        else:
            raise Exception("Please specify the address or the name of the device.")

        return is_connected

if __name__ == "__main__":
    approx_name = "Galaxy Buds"
    device_manager = DeviceInfo()
    
    # conndevs = device_manager.connected_devices
    # logger.info(conndevs)
    
    name = device_manager.get_similar_device_names(approx_name)[0]
    logger.info(name)

    address = device_manager.get_device_address(name)
    logger.info(address)

    is_conn = device_manager.is_device_connected(address=address)
    logger.info(f"Is conn: {is_conn}")
