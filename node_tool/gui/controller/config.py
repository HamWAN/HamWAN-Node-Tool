from . import helper;
from PySide import QtGui
from ...models import Configuration

class Window:
    def __init__(self):
        self.MainWindow = helper.loadUiWidget("node_tool/gui/view/config.ui")
        
        generate_configuration_push_button = self.MainWindow.findChild(QtGui.QPushButton, "generate_configuration_push_button")

        generate_configuration_push_button.clicked.connect(self.generate_configuration_push_button_pressed)
        
        self.MainWindow.show()
        return
    def generate_configuration_push_button_pressed(self):
        tabs = self.MainWindow.findChild(QtGui.QTabWidget, "tabWidget")
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
        tabs.setTabEnabled(1, True)
        tabs.setCurrentIndex(1)
        return