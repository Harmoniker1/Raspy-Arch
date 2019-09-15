# --------------------
# startMC.py
# 
# Start a thread in MC
# --------------------

import sys
sys.path.append("..")

from mcpi.minecraft import Minecraft

def start(port = -1) -> Minecraft:
    print('''###########################################
#                                         #
#    Raspy-Arch Control Initialization    #
#                                         #
###########################################
''')
    if port == -1:
        while True:
            try:
                port = int(input("Please specify the natapp port if given; input 0 to connect to local host: "))
            except ValueError:
                print("That wasn't a valid integer.")
            else:
                break
    if port:
        mc = Minecraft.create("server.natappfree.cc", port)
    else:
        mc = Minecraft.create()
    print('Minecraft connection "mc" established!')
    return mc

def test():
    mc = start(0)
    mc.postToChat("Welcome to Howard-C's individual arch project, using raspy control.")
