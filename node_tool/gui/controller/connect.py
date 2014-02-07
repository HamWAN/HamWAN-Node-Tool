from . import helper;

class Window:
    def __init__(self):
        self.MainWindow = helper.loadUiWidget("node_tool/gui/view/connect.ui")
        self.MainWindow.show()
        return
    
    