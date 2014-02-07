from . import helper;
from PySide import QtGui


class Window:
    def __init__(self):
        self.MainWindow = helper.loadUiWidget("node_tool/gui/view/connect.ui")
        ip_address_lineedit = self.MainWindow.findChild(QtGui.QLineEdit, "ip_address_lineedit")
        user_lineedit = self.MainWindow.findChild(QtGui.QLineEdit, "user_lineedit")
        password_lineedit = self.MainWindow.findChild(QtGui.QLineEdit, "password_lineedit")
        connect_pushbutton = self.MainWindow.findChild(QtGui.QPushButton, "connect_pushbutton")

        connect_pushbutton.clicked.connect(self.connection_pressed)

        self.MainWindow.show()
        return
    def connection_pressed(self):
        print("Yo")
        return