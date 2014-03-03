from PySide import QtGui

from .controller import config
import sys

def do():
        
    app = QtGui.QApplication(sys.argv)
    Connect = config.Window()
    # Run the main Qt loop
    sys.exit(app.exec_())
    return
    