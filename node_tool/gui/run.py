from PySide import QtGui

from .controllers import helper
from .controllers import connect
import sys

def do():
        
    app = QtGui.QApplication(sys.argv)
#     MainWindow = helper.loadUiWidget("node_tool/gui/views/connect.ui")
#     MainWindow.show()
    connect.doit()
    # Run the main Qt loop
    sys.exit(app.exec_())
    return
    