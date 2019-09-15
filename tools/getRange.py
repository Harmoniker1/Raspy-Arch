# --------------------
# getRange.py
# 
# Get a list of six numbers indicating the range of the architecture the user want to attach
# --------------------

import sys
sys.path.append("..")

# --------------------
# helpRange
# --------------------

def helpRange(gameName, id):
    """Help the user by giving instructions"""

    print("\nDon't know how to input? I'll help you out.")
    gameName.entity.setRotation(id, 270)
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
# inputRange
# --------------------

def inputRange(gameName, id, info: str):
    """The workflow of inputing a list of number"""

    gameName.postToChat("")
    gameName.postToChat(info + " (in the command line)")
    gameName.postToChat("If you want to know how to input, input 1 instead.")

    print("\n" + info)
    print("If you want to know how to input, input 1 instead.\n")

    gameName.entity.setRotation(id, 270)

    while True:
        numList = [x for x in input().split()]
        if len(numList) == 1:
            try:
                numListInt = int(numList[0])
            except ValueError:
                print("\nYour input doesn't indicate six elements. Please input again.\n")
                continue
            else:
                if numListInt == 1:
                    helpRange(gameName, id)
                    continue
                else:
                    print("\nYour input doesn't indicate six elements. Please input again.\n")
                    continue
        if len(numList) != 6:
            print("\nYour input doesn't indicate six elements. Please input again.\n")
            continue
        try:
            numListInt = [int(x) for x in numList]
        except ValueError:
            print("\nYour input contains non-numerical elements. Please input again.\n")
            continue
        else:
            return numListInt

# --------------------
# orderRange
# --------------------

def orderRange(range: list):
    if len(range) != 6:
        return []
    else:
        if range[0] >= range[3]:
            range = [range[3], range[1], range[2], range[0], range[4], range[5]]
        if range[1] >= range[4]:
            range = [range[0], range[4], range[2], range[3], range[1], range[5]]
        if range[2] >= range[5]:
            range = [range[0], range[1], range[5], range[3], range[4], range[2]]
        return range
