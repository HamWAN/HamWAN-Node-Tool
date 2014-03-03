from . import helper;
from PySide import QtGui, QtCore
from ...models import Configuration
from ...common import helpers
import time

class Window:
    def __init__(self):
        #First we need to link the GUI to some variables
        #Overall Frame
        self.MainWindow = helper.loadUiWidget("node_tool/gui/view/config.ui")
        self.tabs = self.MainWindow.findChild(QtGui.QTabWidget, "tabWidget")
        self.status_bar = self.MainWindow.findChild(QtGui.QStatusBar, "statusbar")
        self.status_bar.showMessage("Waiting to generate configuration.")
        
        #Generate Config page
        self.operators_callsign_line_edit = self.MainWindow.findChild(QtGui.QLineEdit, "operators_callsign_line_edit")
        self.operators_location_line_edit = self.MainWindow.findChild(QtGui.QLineEdit, "operators_location_line_edit")
        self.site_connecting_to_line_edit = self.MainWindow.findChild(QtGui.QLineEdit, "site_connecting_to_line_edit")
        self.newAdminPasswordLineEdit = self.MainWindow.findChild(QtGui.QLineEdit, "newAdminPasswordLineEdit")
        self.shared_administration_check_box = self.MainWindow.findChild(QtGui.QCheckBox, "shared_administration_check_box")
        self.route_cache_bug_fix_check_box = self.MainWindow.findChild(QtGui.QCheckBox, "route_cache_bug_fix_check_box")
        self.dhcp_client_on_lan_check_box = self.MainWindow.findChild(QtGui.QCheckBox, "dhcp_client_on_lan_check_box")
        self.generate_configuration_push_button = self.MainWindow.findChild(QtGui.QPushButton, "generate_configuration_push_button")
        
        self.generate_configuration_push_button.clicked.connect(self.generate_configuration_push_button_pressed)
        
        #Review Config page
        self.review_config_plain_text_edit = self.MainWindow.findChild(QtGui.QPlainTextEdit, "review_config_plain_text_edit")
        self.send_to_router_push_button = self.MainWindow.findChild(QtGui.QPushButton, "send_to_router_push_button")
        self.saveToFilePushButton = self.MainWindow.findChild(QtGui.QPushButton, "saveToFilePushButton")
        
        self.send_to_router_push_button.clicked.connect(self.send_to_router_push_button_pressed)
        self.saveToFilePushButton.clicked.connect(self.saveToFilePushButtonPressed)
        
        #Send to Router page
        self.download_routeros_push_button = self.MainWindow.findChild(QtGui.QPushButton, "download_routeros_push_button")
        self.updateRouterOSPushButton = self.MainWindow.findChild(QtGui.QPushButton, "updateRouterOSPushButton")
        self.ipAddressLineEdit = self.MainWindow.findChild(QtGui.QLineEdit, "ipAddressLineEdit")
        self.usernameLineEdit = self.MainWindow.findChild(QtGui.QLineEdit, "usernameLineEdit")
        self.passwordLineEdit = self.MainWindow.findChild(QtGui.QLineEdit, "passwordLineEdit")
        self.send_progress_bar = self.MainWindow.findChild(QtGui.QProgressBar, "send_progress_bar")
        self.rebootRouterPushButton = self.MainWindow.findChild(QtGui.QPushButton, "rebootRouterPushButton")
        self.configureRouterPushButton = self.MainWindow.findChild(QtGui.QPushButton, "configureRouterPushButton")
        
        self.configureRouterPushButton.clicked.connect(self.configureRouterPushButtonPressed)
        self.download_routeros_push_button.clicked.connect(self.download_routeros_push_button_pressed)
        self.updateRouterOSPushButton.clicked.connect(self.updateRouterOSPushButtonPressed)
        self.rebootRouterPushButton.clicked.connect(self.rebootRouterPushButtonPressed)
        
        #Verify Connection page
        self.MainWindow.show()
        return
    def generate_configuration_push_button_pressed(self):       
        configuration = Configuration(self.operators_callsign_line_edit.text(), self.site_connecting_to_line_edit.text(), self.operators_location_line_edit.text(),
                                       self.newAdminPasswordLineEdit.text(), self.shared_administration_check_box.isChecked(), 
                                       self.dhcp_client_on_lan_check_box.isChecked(), self.route_cache_bug_fix_check_box.isChecked())
        
        self.review_config_plain_text_edit.setPlainText(str(configuration))
        self.tabs.setCurrentIndex(1)
        self.status_bar.showMessage("Configuration generated; review and revise, then save or send to router.")
        return
    def download_routeros_push_button_pressed(self):
        self.status_bar.showMessage("Downloading RouterOS from MikroTik's website...")
        self.send_progress_bar.setMinimum(0)
        self.send_progress_bar.setMaximum(0)
        self.worker = DownloadWorker()
        self.worker.finished.connect(self.finishedDownloading)
        self.worker.start()
        return
    def send_to_router_push_button_pressed(self):
        self.tabs.setCurrentIndex(2)
        self.status_bar.showMessage("Preparing to send configuration to router.")
        return
    def saveToFilePushButtonPressed(self):
        fileName, selectedFilter = QtGui.QFileDialog.getSaveFileName()
        if fileName:
            saveFile = open(fileName, 'w')
            saveFile.write(self.review_config_plain_text_edit.toPlainText())
        return
    def finishedDownloading(self):
        self.send_progress_bar.setMaximum(100)
        if self.worker.status:
            self.send_progress_bar.setValue(25)
            self.status_bar.showMessage("Done downloading RouterOS; now press update RouterOS.")
        else:
            self.send_progress_bar.setValue(0)
            self.status_bar.showMessage("Error downloading RouterOS! Manually add firmware to firmware directory, then press update RouterOS.")
    def updateRouterOSPushButtonPressed(self):
        self.status_bar.showMessage("Uploading files to update...")
        self.send_progress_bar.setMinimum(0)
        self.send_progress_bar.setMaximum(0)
        self.worker = UploadWorker(self.ipAddressLineEdit.text(), self.usernameLineEdit.text(), self.passwordLineEdit.text())
        self.worker.finished.connect(self.finishedUploading)
        self.worker.start()
        return
    def rebootRouterPushButtonPressed(self):
        self.status_bar.showMessage("Requesting that the router reboot...")
        self.send_progress_bar.setMinimum(0)
        self.send_progress_bar.setMaximum(0)
        self.worker = RebootWorker(self.ipAddressLineEdit.text(), self.usernameLineEdit.text(), self.passwordLineEdit.text())
        self.worker.finished.connect(self.finishedRebooting)
        self.worker.start()
        return
    def finishedUploading(self):
        self.send_progress_bar.setMaximum(100)
        if self.worker.status:
            self.send_progress_bar.setValue(50)
            self.status_bar.showMessage("Done uploading updates! Once the router is reset, the updates will take effect.")
        else:
            self.send_progress_bar.setValue(0)
            self.status_bar.showMessage("Error updating RouterOS! Maybe the router connection details are wrong?")
    def finishedRebooting(self):
        self.send_progress_bar.setMaximum(100)
        if self.worker.status:
            self.send_progress_bar.setValue(75)
            self.status_bar.showMessage("Reboot command successfully sent! Wait about 30 seconds for the double-beep and the green light.")
        else:
            self.send_progress_bar.setValue(0)
            self.status_bar.showMessage("Error telling router to reboot! Maybe the router connection details are wrong?")
        return
    def configureRouterPushButtonPressed(self):
        if self.review_config_plain_text_edit.toPlainText():
            self.status_bar.showMessage("Sending configuration to the router...")
            self.send_progress_bar.setMinimum(0)
            self.send_progress_bar.setMaximum(0)
            self.worker = ConfigureWorker(self.ipAddressLineEdit.text(), self.usernameLineEdit.text(), self.passwordLineEdit.text(), self.review_config_plain_text_edit.toPlainText())
            self.worker.finished.connect(self.finishedConfiguring)
            self.worker.start()
        else:
            errorDialog = QtGui.QMessageBox()
            errorDialog.setIcon(QtGui.QMessageBox.Icon.Warning)
            errorDialog.setText('To send a configuration, you must have a configuration! Use the "Generate Config" tab first.')
            errorDialog.exec_()
        return
    def finishedConfiguring(self):
        self.send_progress_bar.setMaximum(100)
        if self.worker.status:
            self.send_progress_bar.setValue(100)
            self.status_bar.showMessage("Configuration complete!")
        else:
            self.send_progress_bar.setValue(0)
            self.status_bar.showMessage("Error configuring the router! Maybe the router connection details are wrong?")
        return

class DownloadWorker(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)
        
    def run(self):
        self.status = helpers.firmware_download()

class UploadWorker(QtCore.QThread):
    def __init__(self, address, username, password):
        self.address = address
        self.username = username
        self.password = password
        QtCore.QThread.__init__(self)
        
    def run(self):
        self.status = helpers.upload_firmware(self.address, self.username, self.password)
        
class RebootWorker(QtCore.QThread):
    def __init__(self, address, username, password):
        self.address = address
        self.username = username
        self.password = password
        QtCore.QThread.__init__(self)
        
    def run(self):            
        self.status = helpers.sshConnect(self.address, self.username, self.password) and helpers.rebootRouter()        
        
class ConfigureWorker(QtCore.QThread):
    def __init__(self, address, username, password, commands):
        self.address = address
        self.username = username
        self.password = password
        self.commands = commands
        QtCore.QThread.__init__(self)
        
    def run(self):            
        self.status = helpers.sshConnect(self.address, self.username, self.password) and helpers.sendCommands(self.commands)