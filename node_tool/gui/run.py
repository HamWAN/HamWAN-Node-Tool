from PySide import QtGui

from .controller import connect
import sys

def do():
        
    app = QtGui.QApplication(sys.argv)
    Connect = connect.Window()
    # Run the main Qt loop
    sys.exit(app.exec_())
    return
    