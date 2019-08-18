# --------------------
# get_range.py
# Get a list of six numbers indicating the range of the architecture the user want to attach
# --------------------

import sys
sys.path.append("..")

# --------------------
# help_range
# --------------------

def help_range(game_name, id):
    """Help the user by giving instructions"""

    print("\nDon't know how to input? I'll help you out.")
    game_name.entity.setRotation(id, 270)
    print("You're now facing the positive side on x-axis.\
 The positive side on z-axis is on your right, while the positive side on y-axis goes into the sky.")
    print("You will have to input the relative coordinate of the diagnoal corners of your architecture.")
    print("It's simple: if you want the architecture to be 5*5 wide, with you being on the center,\
 and 5 blocks tall, with the top of it being on the same height with you, you can simply input:\
 '-2 -4 -2 2 0 2'. The first three numbers are the relative coordinate for the corner at the bottom,\
 and the last three are for the corner at the top. Then, if you're standing on [x, y, z] = [600, 64, 600],\
 your architecture will be attached between [598, 60, 598] and [602, 64, 602].")
    print("This instruction doesn't affect the workflow. Input your six numbers to continue!\n")

# --------------------
# input_range
# --------------------

def input_range(game_name, id, info: str):
    """The workflow of inputing a list of number"""

    game_name.postToChat("")
    game_name.postToChat(info)
    game_name.postToChat("If you want to know how to input, input 1 instead.")
    game_name.postToChat("")

    print("\n" + info)
    print("If you want to know how to input, input 1 instead.\n")

    game_name.entity.setRotation(id, 270)

    while True:
        num_list = [x for x in input().split()]
        if len(num_list) == 1:
            try:
                num_list_int = int(num_list[0])
            except ValueError:
                print("\nYour input doesn't indicate six elements. Please input again.\n")
                continue
            else:
                if num_list_int == 1:
                    help_range(game_name, id)
                    continue
                else:
                    print("\nYour input doesn't indicate six elements. Please input again.\n")
                    continue
        if len(num_list) != 6:
            print("\nYour input doesn't indicate six elements. Please input again.\n")
            continue
        try:
            num_list_int = [int(x) for x in num_list]
        except ValueError:
            print("\nYour input contains non-numerical elements. Please input again.\n")
            continue
        else:
            return num_list_int
