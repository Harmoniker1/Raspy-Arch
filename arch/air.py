# --------------------
# air.py
# 
# Clear a user-defined area by placing air
# --------------------

import sys
sys.path.append("..")

import mcpi.block as block

from tools.startMC import start
from tools.getName import inputName
from tools.getRange import inputRange
from tools.touchVoid import airVoid
from tools.setBlockBesideLoc import setBlocksBesideLoc

mc = start(0)

id = inputName(mc)

while True:

    range = inputRange(mc, id, "Please input the range of the area you want to clear.")
    loc = mc.entity.getPos(id)

    result = airVoid(range, loc, mc)
    if result == "continue":
        continue
    elif result == "break":
        setBlocksBesideLoc(mc, loc, range, block.AIR.id)
        break

print("\nSuccess! Please wait until the work is finished.")
mc.postToChat("")
mc.postToChat("Success! Please wait until the work is finished.")
