'''
Created on Feb 6, 2014

@author: ryan_turner
'''

import os
import zipfile
import urllib
import paramiko
import socket

ssh = paramiko.SSHClient()

def firmware_download():
    if not os.path.exists("firmware"):
        os.makedirs("firmware")
    # Download the mikrotik routeros firmware
    try:
        urllib.urlretrieve("http://download2.mikrotik.com/routeros/6.9/all_packages-mipsbe-6.9.zip", "firmware/all_packages-mipsbe-6.9.zip")
    except:
        print("Error downloading firmware.")
        return False
    try:
        with zipfile.ZipFile("firmware/all_packages-mipsbe-6.9.zip") as zipped_firmware:
            zipped_firmware.extractall("firmware")
    except:
        print("Error unzipping firmware.")
        return False
    try:
        os.remove("firmware/all_packages-mipsbe-6.9.zip")
    except:
        print("Error deleting firmware zip file.")
        return False
        
    # Get the branding package too
    try:
        urllib.urlretrieve("https://github.com/HamWAN/hamwan-branding/raw/master/Mikrotik%20Rebranding/HamWAN-2.9.48.dpk", "firmware/HamWAN-2.9.48.dpk")
    except:
        print("Error downloading branding package.")
        return False
    
    # Get the SSH keys
    try:
        urllib.urlretrieve("https://www.hamwan.org/t/tiki-download_wiki_attachment.php?attId=148&download=y", "firmware/key-dsa-monitoring.txt")
        urllib.urlretrieve("https://www.hamwan.org/t/tiki-download_wiki_attachment.php?attId=140&download=y", "firmware/key-dsa-osburn.txt")
        urllib.urlretrieve("https://www.hamwan.org/t/tiki-download_wiki_attachment.php?attId=123&download=y", "firmware/key-dsa-NQ1E.txt")
        urllib.urlretrieve("https://www.hamwan.org/t/tiki-download_wiki_attachment.php?attId=120&download=y", "firmware/key-dsa-nigel.txt")
        urllib.urlretrieve("https://www.hamwan.org/t/tiki-download_wiki_attachment.php?attId=119&download=y", "firmware/key-dsa-eo.txt")
    except:
        print("Error downloading SSH keys.")
        return False
    return True
def upload_firmware(server, username, password):
    from ftplib import FTP
    ftp = FTP(server)
    try:
        ftp.login(username, password)
    except:
        print("Error logging in to FTP")
        return False
    for filename in os.listdir("firmware"):
        try:
            ftp.storbinary("STOR " + filename, open("firmware/" + filename, "rb"))
        except:
            print("Error uploading file " + filename)
            return False
    ftp.close()
    return True
def sshConnect(server, username, password):
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(server, username=username, password=password)
    except paramiko.AuthenticationException:
        print ("Bad auth")
        return False
    except socket.error:
        print("Socket error")
        return False
    return True
def sshDisconnect():
    ssh.close()
    return
def rebootRouter():
    stdin, stdout, stderr = ssh.exec_command("/system reboot")
    stdin.write('y\n')
    stdin.flush()
    return True
def sendCommands(commands):
    for line in commands.splitlines():
        ssh.exec_command(line)
    return True