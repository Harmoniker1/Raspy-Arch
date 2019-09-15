# --------------------
# fillBedrock.py
# 
# Fill possible holes with bedrock in a large area beside the player
# --------------------

import sys
sys.path.append("..")

import mcpi.block as block

from tools.startMC import start
from tools.getName import inputName
from tools.setBlockBesideLoc import setBlocksBesideLoc

mc = start(0)

id = inputName(mc)
loc = mc.entity.getPos(id)

setBlocksBesideLoc(mc, loc, [-999, 1, -999, 999, 1, 999], block.BEDROCK.id)
print("\nSucceeded!")
mc.postToChat("")
mc.postToChat("Succeeded!")
