import numpy as np
from IN3140_task1a_fridatbe import forward
from IN3140_task1b_fridatbe import inverse

joint_angles_test = np.array([[0,0,0]])

print("Task1c: \nTests:")
print("sending in: \n", joint_angles_test[0])
cart_output = np.round(forward(joint_angles_test),4)
print("after forward: \n", cart_output[0])
joints_output = np.round(inverse(cart_output[0]),4)
print("after inverse: \n", joints_output)

joint_angles_test = np.array([[270,-30,45]])
print("\nTask1c: \nTests:")
print("sending in: \n", joint_angles_test[0])
cart_output = np.round(forward(joint_angles_test),4)
print("after forward: \n", cart_output[0])
joints_output = np.round(inverse(cart_output[0]),4)
print("after inverse: \n", joints_output)


# if one of the sets of cartesian coordinates correspons to the input to forward, ythe two functions work as they should
# output-example
# Task1c:
# Tests:
# sending in:
#  [0 0 0]
# after forward:
#  [358.3   0.  100.9]
# D  1.0
# after inverse:
#  [[  0.  -0.   0.]
#  [  0.  -0.  -0.]
#  [180. 180.   0.]
#  [180. 180.  -0.]]