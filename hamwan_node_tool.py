if __name__ == '__main__':
#     from node_tool.common.helpers import firmware
#     Firmware = firmware()
#     Firmware.download()
#     print("done")
    
    #To-Do: Switch between CLI and GUI; for now, defaulting to GUI
    from node_tool.gui import run
    run.do()