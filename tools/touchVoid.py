# --------------------
# touchVoid.py
# 
# If the to-be-generated architecture will cause a hole straight down to the void,
# prevent the user from doing so or inform the user
#
# If the to-be-generated architecture cannot be generated entirely due to the bottom limit,
# prevent the user from doing so
# --------------------

import sys
sys.path.append("..")

import mcpi.block as block

from tools.setBlockBesideLoc import setBlocksBesideLoc

# --------------------
# airVoid
# --------------------

def airVoid(range: list, loc, gameName):

    if loc.y + range[1] <= 0 or loc.y + range[4] <= 0:
        if (range[0] <= 0 <= range[3] or range[3] <= 0 <= range[0]) and (range[2] <= 0 <= range[5] or range[5] <= 0 <= range[2]):
            print("\nThis may cause a hole straight down to the void, into which you will fall down and die. Please input again.")
            return "continue"
        else:
            print("\nThis may cause a hole straight down to the void. You'll not fall down into it, but do you wish to proceed?")
            a = input("Input 0 to abort and input again, or input anything else to proceed.\n\n")
            try:
                aInt = int(a)
            except ValueError:
                return "break"
            else:
                if aInt == 0:
                    return "continue"
                else:
                    return "break"
    
    else:
        return "break"

# --------------------
# poolVoid
# --------------------

def poolVoid(range: list, loc, gameName):
    if loc.y + range[1] <= -1 or loc.y + range[4] <= -1:
        print("\nThe pool cannot be generated this low (or deep) because of the bottom limit of the world. Please input again.")
        return "continue"
    else:
        return "break"
