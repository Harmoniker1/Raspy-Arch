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
from tools.preventVoid import preventVoid
from tools.setBlockBesideLoc import setBlocksBesideLoc