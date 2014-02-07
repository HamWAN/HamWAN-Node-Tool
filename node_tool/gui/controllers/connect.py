from PySide import QtGui
from . import helper;


def doit():
    MainWindow = helper.loadUiWidget("node_tool/gui/views/connect.ui")
    MainWindow.show()
    print("yo")
    return
    