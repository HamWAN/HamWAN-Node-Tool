if __name__ == '__main__':
#     from node_tool.common.helpers import firmware
#     Firmware = firmware()
#     Firmware.download()
#     print("done")
    from PySide import QtGui
    from PySide import QtCore
    from PySide import QtUiTools

    import sys
    
    #To-Do: Switch between CLI and GUI; for now, defaulting to GUI


    # Create and show the form
    def loadUiWidget(uifilename, parent=None):
        loader = QtUiTools.QUiLoader()
        file = QtCore.QFile(uifilename)
        file.open(QtCore.QFile.ReadOnly)
        ui = loader.load(file, parent)
        file.close()
        return ui
            
        
    app = QtGui.QApplication(sys.argv)
    MainWindow = loadUiWidget("node_tool/gui/views/connect.ui")
    MainWindow.show()
    # Run the main Qt loop
    sys.exit(app.exec_())