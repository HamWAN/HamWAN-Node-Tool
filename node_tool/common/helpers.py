'''
Created on Feb 6, 2014

@author: ryan_turner
'''
import urllib.request
import shutil
import os
import zipfile

class firmware(object):
    
    def download(self):
        directory = "firmware"
        if not os.path.exists(directory):
            os.makedirs(directory)
        # Download the mikrotik routeros firmware
        file_name = "all_packages-mipsbe-6.9.zip"
        url = "http://download2.mikrotik.com/routeros/6.9/"
        try:
            with urllib.request.urlopen(url + file_name) as response, open(directory + "/" + file_name, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)
        except Exception as e:
            print("Error downloading firmware.")
        try:
            with zipfile.ZipFile(directory + "/" + file_name) as zipped_firmware:
                zipped_firmware.extractall(directory)
        except Exception as e:
            print("Error unzipping firmware.")
        try:
            os.remove(directory + "/" + file_name)
        except Exception as e:
            print("Error deleting firmware zip file.")
            
        # Get the branding package too
        file_name = "HamWAN-2.9.48.dpk"
        url = "https://github.com/HamWAN/hamwan-branding/raw/master/Mikrotik%20Rebranding/"
        try:
            with urllib.request.urlopen(url + file_name) as response, open(directory + "/" + file_name, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)
        except Exception as e:
            print("Error downloading branding package.")
        
        return
    
    def __init__(self):
        '''
        Constructor
        '''

