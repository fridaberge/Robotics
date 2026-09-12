import numpy as np
from sympy import *

#konstants
d1 = 100.9
a2 = 222.1
a3 = 136.2

#input angle-sets
joint_angles = np.array(
                        [[270, -30, 45],
                         [270, -30, -45],
                         [0,0,0],
                         [30, 50, 60]])

#converts from degrees to radians
def degToRad(deg):
    return deg*(np.pi/180)

#the function that does the forward kinematic calculations
def forward(joint_angles):
    cartesian = [0 for i in range(len(joint_angles))]
    index = 0
    for angles in joint_angles:
        cartSet = [0]*3
        cartSet[0] = np.round(a3*np.cos(degToRad(angles[0]))*np.cos(degToRad(angles[1]))*np.cos(degToRad(angles[2]))-a3*np.cos(degToRad(angles[0]))*np.sin(degToRad(angles[1]))*np.sin(degToRad(angles[2]))+a2*np.cos(degToRad(angles[0]))*np.cos(degToRad(angles[1])), 1)
        cartSet[1] = np.round(a3*np.sin(degToRad(angles[0]))*np.cos(degToRad(angles[1]))*np.cos(degToRad(angles[2]))-a3*np.sin(degToRad(angles[0]))*np.sin(degToRad(angles[1]))*np.sin(degToRad(angles[2]))+a2*np.sin(degToRad(angles[0]))*np.cos(degToRad(angles[1])), 1)
        cartSet[2] = np.round(-a3*np.sin(degToRad(angles[1]))*np.cos(degToRad(angles[2]))-a3*np.cos(degToRad(angles[1]))*np.sin(degToRad(angles[2]))-a2*np.sin(degToRad(angles[1]))+d1, 1)
        cartesian[index] = cartSet
        index = index+1
    return cartesian

cart_cord = forward(joint_angles)
# print(cart_cord)

y = 100
x = 50
z = 150
l1 = 200
l2 = 100
l3 = 300

first = np.arctan2(-l2,l3)
D = (l3**2)+(l2**2)-((z-l1)**2)
print(D)
last = np.arctan2(np.sqrt(D),z-l1)
print(np.rad2deg(first+last))

r = x**2+y**2
d = np.sqrt(r+(z-l1)**2)
# print(1-(l2/d)**2)
alpha = np.arctan2(np.sqrt(1-(l2/d)**2),l2/d)
betha = np.arctan2(np.sqrt(r),z-l1)
print(np.rad2deg(alpha+betha))




# print("cos = ",np.round(np.cos(90*np.pi/180),2))

# A = np.array([[1,2,4,8],
#             [1,3,9,27],
#             [1,4,16,64],
#             [1,5,25,125],
#             [1,6,36,216]])
# AT = A.transpose()
# b = np.array([[7],
#              [3],
#              [5],
#              [4],
#              [3]])
# ATA = AT@A
# ATb = AT@b

# likn = np.column_stack((ATA, ATb))
# los = Matrix(likn).rref()

# print(f'A:\n{A}')
# print(f'AT:\n{AT}')
# print(f'b:\n{b}')
# print(f'ATA:\n{ATA}')
# print(f'ATb:\n{ATb}')
# print(f'likning:\n{likn}')
# print(f'ATb:\n{los}')
  