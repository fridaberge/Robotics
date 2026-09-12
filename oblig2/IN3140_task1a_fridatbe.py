import numpy as np

#konstants
d1 = 100.9
a2 = 222.1
a3 = 136.2

#converts from degrees to radians
def degToRad(deg):
    return deg*(np.pi/180)

#the function that does the forward kinematic calculations
def forward(joint_angles):
    cartesian = [0 for i in range(len(joint_angles))]
    index = 0
    for angles in joint_angles:
        cartSet = [0]*3
        cartSet[0] = a3*np.cos(degToRad(angles[0]))*np.cos(degToRad(angles[1]))*np.cos(degToRad(angles[2]))-a3*np.cos(degToRad(angles[0]))*np.sin(degToRad(angles[1]))*np.sin(degToRad(angles[2]))+a2*np.cos(degToRad(angles[0]))*np.cos(degToRad(angles[1]))
        cartSet[1] = a3*np.sin(degToRad(angles[0]))*np.cos(degToRad(angles[1]))*np.cos(degToRad(angles[2]))-a3*np.sin(degToRad(angles[0]))*np.sin(degToRad(angles[1]))*np.sin(degToRad(angles[2]))+a2*np.sin(degToRad(angles[0]))*np.cos(degToRad(angles[1]))
        cartSet[2] = -a3*np.sin(degToRad(angles[1]))*np.cos(degToRad(angles[2]))-a3*np.cos(degToRad(angles[1]))*np.sin(degToRad(angles[2]))-a2*np.sin(degToRad(angles[1]))+d1
        cartesian[index] = cartSet
        index = index+1
    return cartesian