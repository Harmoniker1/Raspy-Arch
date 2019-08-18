# --------------------
# get_range.py
# Get the user's name
# --------------------

import sys
sys.path.append("..")

import mcpi.connection

# --------------------
# input_name
# --------------------

def input_name(game_name):
    """The workflow of inputing the user's name"""

    game_name.postToChat("")
    game_name.postToChat("Please input your name in the command line to initiate the program.")
    game_name.postToChat("")

    print("\nPlease input your name to initiate the program.\n")

    while True:
        name = input()
        try:
            id = game_name.getPlayerEntityId(name)
        except mcpi.connection.RequestError:
            print("\nWrong name, please input again:\n")
            continue
        else:
            return id
