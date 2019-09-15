# --------------------
# getName.py
# 
# Get the user's name
# --------------------

import sys
sys.path.append("..")

import mcpi.connection

# --------------------
# inputName
# --------------------

def inputName(gameName):
    """The workflow of inputing the user's name"""

    gameName.postToChat("")
    gameName.postToChat("Please input your name in the command line to initiate the program.")

    print("\nPlease input your name to initiate the program.\n")

    while True:
        name = input()
        try:
            id = gameName.getPlayerEntityId(name)
        except mcpi.connection.RequestError:
            print("\nWrong name, please input again:\n")
            continue
        else:
            return id
