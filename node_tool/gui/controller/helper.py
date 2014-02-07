from PySide import QtCore
from PySide import QtUiTools


def loadUiWidget(uifilename, parent=None):
    loader = QtUiTools.QUiLoader()
    file = QtCore.QFile(uifilename)
    file.open(QtCore.QFile.ReadOnly)
    ui = loader.load(file, parent)
    file.close()
    return ui