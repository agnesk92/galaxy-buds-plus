import bluetooth


def get_battery_levels(bltooth_address): 
    uuid = "00001101-0000-1000-8000-00805F9B34FB"
    service_matches = bluetooth.find_service(uuid=uuid, address=bltooth_address)

    host = service_matches[0]["host"]
    port = service_matches[0]["port"]
    
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((host, port))
    
    data = sock.recv(1024)
    batterylife = None
    while data[3] not in [96, 97] and len(data) != 0:
        print(f"Data battery elem: {data[3]}")
        
        data = sock.recv(1024)
        print(len(data))
        if data[3] == 97:
            batterylife = (data[6], data[7], data[11])
        if data[3] == 96:
            batterylife = (data[5], data[6], data[10])
        
    if batterylife is None:
        raise Exception("Couldn't get battery info")

    return batterylife


if __name__ == "__main__":
    "34:82:C5:31:5D:B1"
    bltooth_address = "34:82:C5:31:5D:B1"
    device_name = bluetooth.lookup_name(bltooth_address)

    uuid = "00001101-0000-1000-8000-00805F9B34FB"
    service_matches = bluetooth.find_service(uuid=uuid, address=bltooth_address)
    host = service_matches[0]["host"]
    port = service_matches[0]["port"]
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((host, port))
    
    data = sock.recv(1024)
    batterylife = None
    while data[3] not in [96, 97] and len(data) != 0:
        print(f"Data battery elem: {data[3]}")
        
        data = sock.recv(1024)
        print(len(data))
        if data[3] == 97:
            batterylife = "{},{},{}".format(data[6], data[7], data[11])
        if data[3] == 96:
            batterylife = "{},{},{}".format(data[5], data[6], data[10])
        # batterylife2 = "{},{},{}".format(data[2], data[3], data[7])
        
        print(str(batterylife))

