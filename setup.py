from distutils.core import setup
import py2exe
includes = []
includes.append("PySide.QtUiTools")
includes.append("PySide.QtXml")

setup(console = ['hamwan_node_tool.py'],
      options = {'py2exe':
                    {'includes':includes}
                }
      )