HamWAN-Node-Tool
================
Dependencies
-------------
* python
* python-pyside
* python-jinja2
* paramiko

Development Tools:
* Eclipse & PyDev
* qt4-designer (for GUI views)

Installation
=============
Ubuntu
-------------
	sudo apt-get install python python-pip python-dev libssh2-1 libssh2-1-dev git
	pip install http://pypi.python.org/packages/source/p/pylibssh2/pylibssh2-1.0.1.tar.gz
	pip install Jinja2
	mkdir ~/hamwan-node-tool
	cd ~/hamwan-node-tool
	git clone https://github.com/HamWAN/HamWAN-Node-Tool.git .
	python hamwan_node_tool.py

Windows
-------------
Install via exe/msi installers:
Python 2.7.6 32 bit
Pyside 1.2.1 win32-py2.7
python pip

Once those are installed, use pip to install the last deps:
pip install pycrypto jinja2 paramiko

Voila! Premade exe coming soon.
