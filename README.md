HamWAN-Node-Tool
================
Dependencies
-------------
* python
* python-pyside
* python-jinja2
* pylibssh2
* ftplib

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
