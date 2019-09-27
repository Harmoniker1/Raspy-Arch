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
from tools.rsetBlock import rsetBlocks

mc = start(0)

id = inputName(mc)
loc = mc.entity.getPos(id)

rsetBlocks(mc, loc, [-99, - loc.y, -99, 99, - loc.y, 99], block.BEDROCK.id)
print("\nSucceeded!")
mc.postToChat("")
mc.postToChat("Succeeded!")
