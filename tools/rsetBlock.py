# --------------------
# rsetBlock.py
# 
# Set block/blocks with the player's location being (0,0,0)
# --------------------

import sys
sys.path.append("..")

def rsetBlock(gameName, loc, point, block, data = 0):
    gameName.setBlock(loc.x + point[0], loc.y + point[1], loc.z + point[2], block, data)

def rsetBlocks(gameName, loc, range, block, data = 0):
    gameName.setBlocks(loc.x + range[0], loc.y + range[1], loc.z + range[2], loc.x + range[3], loc.y + range[4], loc.z + range[5], block, data)
