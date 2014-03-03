'''
Created on Feb 6, 2014

@author: ryan_turner
'''

import os
import zipfile
import urllib

def firmware_download():
    directory = "firmware"
    if not os.path.exists(directory):
        os.makedirs(directory)
    # Download the mikrotik routeros firmware
    file_name = "all_packages-mipsbe-6.9.zip"
    url = "http://download2.mikrotik.com/routeros/6.9/"
    try:
        urllib.urlretrieve(url + file_name, directory + "/" + file_name)
    except:
        print("Error downloading firmware.")
        return False
    try:
        with zipfile.ZipFile(directory + "/" + file_name) as zipped_firmware:
            zipped_firmware.extractall(directory)
    except:
        print("Error unzipping firmware.")
        return False
    try:
        os.remove(directory + "/" + file_name)
    except:
        print("Error deleting firmware zip file.")
        return False
        
    # Get the branding package too
    file_name = "HamWAN-2.9.48.dpk"
    url = "https://github.com/HamWAN/hamwan-branding/raw/master/Mikrotik%20Rebranding/"
    try:
        urllib.urlretrieve(url + file_name, directory + "/" + file_name)
    except:
        print("Error downloading branding package.")
        return False
    return True
        

