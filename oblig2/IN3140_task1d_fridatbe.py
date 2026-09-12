import numpy as np
from task1b import inverse

#konstants
d1 = 100.9
a2 = 222.1
a3 = 136.2

#input angle-sets
cart_cord = [0, -323.9033, 176.6988]

joint_angles = np.round(inverse(cart_cord), 4)
print("Task 1d:\n", joint_angles)

# output:
# Task 1d:
#  [[-90.     -29.9999  44.9997]
#  [-90.       3.6576 -44.9997]
#  [ 90.     209.9999  44.9997]
#  [ 90.     176.3424 -44.9997]]