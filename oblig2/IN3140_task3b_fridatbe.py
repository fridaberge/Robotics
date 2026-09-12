import numpy as np
from task3a import jacobian

joint_angles_test = [-90, -30, 45]
joint_velocities_test = [0.1, 0.05, 0.05]

print("task 3b:")
cart_velocities = jacobian(joint_angles_test, joint_velocities_test)
print(np.round(cart_velocities,4))

# output:
# task 3b:
# [[ 32.3903]
#  [ -2.0274]
#  [-22.7731]]