""" Simple GUI for showing battery level for Galaxy Buds Plus device """
import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QAction, QApplication, QSystemTrayIcon, QMenu, QWidget

from battery import get_battery_levels
from devices import DeviceInfo


def get_earbud_battery_info(): 
    approx_name = "Galaxy Buds"

    device_man = DeviceInfo()
    device_name = device_man.get_similar_device_names(approx_name)[0]
    device_address = device_man.get_device_address(device_name)

    return get_battery_levels(device_address) 
    

class SystemTrayIcon(QSystemTrayIcon):

    def __init__(self, icon, parent=None, app=None): 
        QSystemTrayIcon.__init__(self, icon, parent)
        
        menu = QMenu(parent)
        self.app = app

        reloadAction = menu.addAction("Reload..")
        reloadAction.triggered.connect(self.load_tooltip)
        
        exitAction = menu.addAction("Exit")
        exitAction.triggered.connect(self.close)
        
        self.setContextMenu(menu)

    def load_tooltip(self):
        print("Getting battery levels..")    
        b_left, b_right, b_case = get_earbud_battery_info()
        tooltip_battery = f"Battery {b_left}%, {b_right}%, {b_case}%"
        
        print(f"Set tooltip with battery levels: {b_left}%, {b_right}%, {b_case}%")    
        self.setToolTip(tooltip_battery)

    def close(self):
        print("Exiting app")
        self.app.quit()
        

def main():
    app = QApplication(sys.argv)
    buds_widget = QWidget()

    trayIcon = SystemTrayIcon(QtGui.QIcon("galaxy-icon.png"), buds_widget, app=app)
    trayIcon.load_tooltip()
    trayIcon.toolTip()
    trayIcon.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
