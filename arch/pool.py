# --------------------
# pool.py
# 
# Generate a swimming pool
#
# You can acquire an edge made by a different block 
# by replacing LIGHT_BLUE_GLAZED_TERRACOTTA with the desired block type
# --------------------

import sys
sys.path.append("..")

import mcpi.block as block

from tools.startMC import start
from tools.getName import inputName
from tools.getRange import inputRange, orderRange
from tools.touchVoid import poolVoid
from tools.setBlockBesideLoc import setBlocksBesideLoc

mc = start(0)

id = inputName(mc)

while True:

    range = inputRange(mc, id, "Please input the range of edge of the pool.")
    loc = mc.entity.getPos(id)

    result = poolVoid(range, loc, mc)

    if result == "continue":
        continue

    elif result == "break":
        
        range = orderRange(range)

        if range[0] + 1 > range[3] - 1 or range[2] + 1 > range[5] - 1 or range[1] == range[4]:
            print("\nThe area you required is so small that there can't even have water in it. Please input again")
            continue

        edges = [[range[0], range[1], range[2], range[0], range[4], range[5]]
            , [range[0], range[1], range[2], range[3], range[4], range[2]]
            , [range[3], range[1], range[2], range[3], range[4], range[5]]
            , [range[0], range[1], range[5], range[3], range[4], range[5]]
            , [range[0], range[1], range[2], range[3], range[1], range[5]]
            ]
        
        for edge in edges:
            setBlocksBesideLoc(mc, loc, edge, block.LIGHT_BLUE_GLAZED_TERRACOTTA.id)
        
        waterRange = [range[0] + 1, range[1] + 1, range[2] + 1, range[3] - 1, range[4], range[5] - 1]
        setBlocksBesideLoc(mc, loc, waterRange, block.WATER_STATIONARY.id)

        break

print("\nSuccess! Please wait until the work is finished.")
mc.postToChat("")
mc.postToChat("Success! Please wait until the work is finished.")
