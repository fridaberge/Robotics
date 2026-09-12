import numpy as np

#konstants
d1 = 100.9
a2 = 222.1
a3 = 136.2

#converts from degrees to radians
def degToRad(deg):
    return deg*(np.pi/180)

#converts from radius to degrees
def radToDeg(rad):
    return rad*(180/np.pi)

#the function that does the forward kinematic calculations
def inverse(cart_cord):
    joint_angles = [0]*4
    x = cart_cord[0]
    y = cart_cord[1]
    z = cart_cord[2]
    D = np.round((x**2+y**2+(z-d1)**2-a2**2-a3**2)/(2*a2*a3),5)
    print("D ", D)

    # solution 1:
    # elbow up
    joint_angles_set1 = [0]*3
    joint_angles_set1[0] = radToDeg(np.arctan2(y,x))
    joint_angles_set1[2] = -radToDeg(-np.arctan2(np.sqrt(1-D**2), D))
    joint_angles_set1[1] = -radToDeg(np.arctan2(z-d1, np.sqrt(x**2+y**2))-np.arctan2(a3*np.sin(degToRad(-joint_angles_set1[2])), a2+a3*np.cos(degToRad(-joint_angles_set1[2]))))
    joint_angles[0] = joint_angles_set1

    # solution 2:
    # elbow down
    joint_angles_set2 = [0]*3
    joint_angles_set2[0] = radToDeg(np.arctan2(y,x))
    joint_angles_set2[2] = -radToDeg(np.arctan2(np.sqrt(1-D**2), D))
    joint_angles_set2[1] = -radToDeg(np.arctan2(z-d1, np.sqrt(x**2+y**2))-np.arctan2(a3*np.sin(degToRad(-joint_angles_set2[2])), a2+a3*np.cos(degToRad(-joint_angles_set2[2]))))
    joint_angles[1] = joint_angles_set2

    # solution 3:
    # elbow up with 180 degrees rotation on theta1
    joint_angles_set3 = [0]*3
    joint_angles_set3[0] = radToDeg(np.arctan2(y,x))+180
    joint_angles_set3[2] = -radToDeg(-np.arctan2(np.sqrt(1-D**2), D))
    joint_angles_set3[1] = 180+radToDeg(np.arctan2(z-d1, np.sqrt(x**2+y**2))-np.arctan2(a3*np.sin(degToRad(-joint_angles_set3[2])), a2+a3*np.cos(degToRad(-joint_angles_set3[2]))))
    joint_angles[2] = joint_angles_set3

    # solution 4:
    # elbow down with 180 degrees rotation on theta1
    joint_angles_set4 = [0]*3
    joint_angles_set4[0] = radToDeg(np.arctan2(y,x))+180
    joint_angles_set4[2] = -radToDeg(np.arctan2(np.sqrt(1-D**2), D))
    joint_angles_set4[1] = 180+radToDeg(np.arctan2(z-d1, np.sqrt(x**2+y**2))-np.arctan2(a3*np.sin(degToRad(-joint_angles_set4[2])), a2+a3*np.cos(degToRad(-joint_angles_set4[2]))))
    joint_angles[3] = joint_angles_set4

    return joint_angles

