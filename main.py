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
    try:
        device_address = device_man.get_device_address(device_name)
        return get_battery_levels(device_address) 
    except Exception as e:
        print("Couldn't get battery info.")
        return None
    

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
        battery_levels = get_earbud_battery_info()
        if battery_levels is not None:
            tooltip_msg = f"Battery {battery_levels[0]}%, {battery_levels[1]}%, {battery_levels[2]}%"
            print(f"Set tooltip with battery levels: {b_left}%, {b_right}%, {b_case}%")    
        else:
            tooltip_msg = "No battery information"

        self.setToolTip(tooltip_msg)

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
