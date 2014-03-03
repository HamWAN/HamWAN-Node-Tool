from . import helper;
from PySide import QtGui, QtCore
from ...models import Configuration
from ...common import helpers
import time

class Window:
    def __init__(self):
        self.MainWindow = helper.loadUiWidget("node_tool/gui/view/config.ui")
        self.tabs = self.MainWindow.findChild(QtGui.QTabWidget, "tabWidget")
        self.status_bar = self.MainWindow.findChild(QtGui.QStatusBar, "statusbar")
        self.status_bar.showMessage("Waiting to generate configuration.")
        generate_configuration_push_button = self.MainWindow.findChild(QtGui.QPushButton, "generate_configuration_push_button")
        download_routeros_push_button = self.MainWindow.findChild(QtGui.QPushButton, "download_routeros_push_button")
        send_to_router_push_button = self.MainWindow.findChild(QtGui.QPushButton, "send_to_router_push_button")
        
        generate_configuration_push_button.clicked.connect(self.generate_configuration_push_button_pressed)
        download_routeros_push_button.clicked.connect(self.download_routeros_push_button_pressed)
        send_to_router_push_button.clicked.connect(self.send_to_router_push_button_pressed)
        
        self.MainWindow.show()
        return
    def generate_configuration_push_button_pressed(self):
        review_config_plain_text_edit = self.MainWindow.findChild(QtGui.QPlainTextEdit, "review_config_plain_text_edit")
        operators_callsign_line_edit = self.MainWindow.findChild(QtGui.QLineEdit, "operators_callsign_line_edit")
        operators_location_line_edit = self.MainWindow.findChild(QtGui.QLineEdit, "operators_location_line_edit")
        site_connecting_to_line_edit = self.MainWindow.findChild(QtGui.QLineEdit, "site_connecting_to_line_edit")
        shared_administration_check_box = self.MainWindow.findChild(QtGui.QCheckBox, "shared_administration_check_box")
        route_cache_bug_fix_check_box = self.MainWindow.findChild(QtGui.QCheckBox, "route_cache_bug_fix_check_box")
        dhcp_client_on_lan_check_box = self.MainWindow.findChild(QtGui.QCheckBox, "dhcp_client_on_lan_check_box")
        
        configuration = Configuration(operators_callsign_line_edit.text(), site_connecting_to_line_edit.text(), operators_location_line_edit.text(),
                                       shared_administration_check_box.isChecked(), dhcp_client_on_lan_check_box.isChecked(), route_cache_bug_fix_check_box.isChecked())
        
        review_config_plain_text_edit.setPlainText(str(configuration))
        self.tabs.setTabEnabled(1, True)
        self.tabs.setCurrentIndex(1)
        self.status_bar.showMessage("Configuration generated; review and revise, then save or send to router.")
        return
    def download_routeros_push_button_pressed(self):
        self.status_bar.showMessage("Downloading RouterOS from MikroTik's website.")
        send_progress_bar = self.MainWindow.findChild(QtGui.QProgressBar, "send_progress_bar")
        send_progress_bar.setMinimum(0)
        send_progress_bar.setMaximum(0)
        self.worker = Worker()
        self.worker.finished.connect(self.finishedDownloading)
        self.worker.start()
        return
    def finishedDownloading(self):
        send_progress_bar = self.MainWindow.findChild(QtGui.QProgressBar, "send_progress_bar")
        send_progress_bar.setMaximum(100)
        if self.worker.status:
            send_progress_bar.setValue(33)
            self.status_bar.showMessage("Done downloading RouterOS; now press update RouterOS.")
        else:
            send_progress_bar.setValue(0)
            self.status_bar.showMessage("Error downloading RouterOS! Manually add firmware to firmware directory, then press update RouterOS.")
            
    def send_to_router_push_button_pressed(self):
        self.tabs.setTabEnabled(2, True)
        self.tabs.setCurrentIndex(2)
        self.status_bar.showMessage("Preparing Qto send configuration to router.")
        return


#Inherit from QThread
class Worker(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)
        
    def run(self):
        self.status = helpers.firmware_download()