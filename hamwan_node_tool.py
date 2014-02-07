if __name__ == '__main__':
#     from node_tool.common.helpers import firmware
#     Firmware = firmware()
#     Firmware.download()
#     print("done")
    from node_tool.gui.views import connect
    from PySide import QtGui
    import sys
    
    #To-Do: Switch between CLI and GUI; for now, defaulting to GUI
    app = QtGui.QApplication(sys.argv)
    # Create and show the form
    form = connect.Window()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())