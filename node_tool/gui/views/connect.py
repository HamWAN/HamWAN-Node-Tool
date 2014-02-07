import sys
from PySide import QtCore
from PySide import QtGui
 
class Window(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.resize(400, 200)
        self.setWindowTitle('HamWAN Node Tool - Connect')
        
        self.ip_lineedit = QtGui.QLineEdit()
        self.ip_label = QtGui.QLabel("IP Address")
        self.user_lineedit = QtGui.QLineEdit()
        self.user_label = QtGui.QLabel("User")
        self.password_lineedit = QtGui.QLineEdit()
        self.password_label = QtGui.QLabel("Password")
        self.connect_pushbutton = QtGui.QPushButton("Connect")        

        layout = QtGui.QFormLayout()
        layout.addRow(self.ip_label, self.ip_lineedit)
        layout.addRow(self.user_label, self.user_lineedit)
        layout.addRow(self.password_label, self.password_lineedit)
        layout.addRow(self.connect_pushbutton)
        self.setLayout(layout)
#         self.connect.clicked.connect(self.greetings)
       
    # Greets the user
    def greetings(self):
        print ("Hello %s" % self.edit.text())        