# --------------------
# air.py
# Clear a user-defined area by placing air
# --------------------

import sys
sys.path.append("..")

import mcpi.block as block

from tools.start_mc import start
from tools.get_name import input_name
from tools.get_range import input_range
from tools.set_block_beside_loc import setBlocksBesideLoc

mc = start(0)

id = input_name(mc)

while True:

    range = input_range(mc, id, "Please input the range of the area you want to clear.")
    loc = mc.entity.getPos(id)

    if (- range[1]) >= (loc.y) or (- range[4]) >= (loc.y):
        if range[0] <= 0 <= range[3] and range[2] <= 0 <= range[5]:
            print("\nThis may cause a hole straight down to the void, into which you will fall down and die. Please input again.")
            
            continue
        else:
            print("\nThis may cause a hole straight down to the void. You'll not fall down into it, but do you wish to proceed?")
            a = input("Input 0 to abort and input again, or input anything else to proceed.\n\n")
            try:
                a_int = int(a)
            except ValueError:
                setBlocksBesideLoc(mc, loc, range, block.AIR.id)
                break
            else:
                if a_int == 0:
                    continue
                else:
                    setBlocksBesideLoc(mc, loc, range, block.AIR.id)
                    break
    
    else:
        setBlocksBesideLoc(mc, loc, range, block.AIR.id)
        break

print("\nSuccess! Please wait until the work is finished.")
mc.postToChat("")
mc.postToChat("Success! Please wait until the work is finished.")
