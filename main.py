""" Simple GUI for showing battery level for Galaxy Buds Plus device """
import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QAction, QApplication, QSystemTrayIcon, QMenu, QWidget

from battery import get_battery_levels
from devices import DeviceInfo


class SystemTrayIcon(QSystemTrayIcon):

    def __init__(self, icon, parent=None, app=None): 
        QSystemTrayIcon.__init__(self, icon, parent)
        
        menu = QMenu(parent)
        self.app = app

        exitAction = menu.addAction("Exit")
        exitAction.triggered.connect(self.close)
        
        self.setContextMenu(menu)

    def close(self):
        print("Exiting app")
        self.app.quit()
        

def get_earbud_info(): 
    approx_name = "Galaxy Buds"
    device_manager = DeviceInfo()
    
    # conndevs = device_manager.connected_devices
    # print(conndevs)
    
    name = device_manager.get_similar_device_names(approx_name)[0]
    print(name)

    address = device_manager.get_device_address(name)
    print(address)

    is_conn = device_manager.is_device_connected(address=address)
    print(f"Is conn: {is_conn}")


def main():
    print("Getting battery levels..")    
    device_man = DeviceInfo()
    device_name = device_man.get_similar_device_names("Galaxy Buds")[0]
    device_address = device_man.get_device_address(device_name)

    b_left, b_right, b_case = get_battery_levels(device_address) 
    # b_left = 95
    # b_right = 95
    # b_case = 17

    print("Create app")
    app = QApplication(sys.argv)
    buds_widget = QWidget()

    print("Creating tray icon..")
    trayIcon = SystemTrayIcon(QtGui.QIcon("galaxy-icon.png"), buds_widget, app=app)

    # tooltip_battery = QtCore.QString("battery level indicator")
    # tooltip_battery = QtCore.RichText("<b>bold</b> text")
    # tooltip_battery = "<b>bold</b> text"
    tooltip_battery = f"Battery {b_left}%, {b_right}%, {b_case}%"
    trayIcon.setToolTip(tooltip_battery)
    trayIcon.toolTip() #.setText("test3")
    trayIcon.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

