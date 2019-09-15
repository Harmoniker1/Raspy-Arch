# --------------------
# preventVoid.py
# 
# If the to-be-generated architecture will cause a hole straight down to the void,
# prevent the user from doing so or inform the user
# --------------------

import sys
sys.path.append("..")

import mcpi.block as block

from tools.setBlockBesideLoc import setBlocksBesideLoc

def preventVoid(range: list, loc, gameName):

    if (- range[1]) >= (loc.y) or (- range[4]) >= (loc.y):
        if (range[0] <= 0 <= range[3] or range[3] <= 0 <= range[0]) and (range[2] <= 0 <= range[5] or range[5] <= 0 <= range[2]):
            print("\nThis may cause a hole straight down to the void, into which you will fall down and die. Please input again.")
            return "continue"
        else:
            print("\nThis may cause a hole straight down to the void. You'll not fall down into it, but do you wish to proceed?")
            a = input("Input 0 to abort and input again, or input anything else to proceed.\n\n")
            try:
                aInt = int(a)
            except ValueError:
                setBlocksBesideLoc(gameName, loc, range, block.AIR.id)
                return "break"
            else:
                if aInt == 0:
                    return "continue"
                else:
                    setBlocksBesideLoc(gameName, loc, range, block.AIR.id)
                    return "break"
    
    else:
        setBlocksBesideLoc(gameName, loc, range, block.AIR.id)
        return "break"
