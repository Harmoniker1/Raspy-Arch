import sys
sys.path.append("..")

from get_name import input_name
from get_range import input_range
from start_mc import start

mc = start(0)

print("\nTest mode.")

id = input_name(mc)

print(input_range(mc, id, "Please input six numbers indicating the range of your architecture."))
