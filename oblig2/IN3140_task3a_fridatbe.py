import numpy as np

#constants
d1 = 100.9
a2 = 222.1
a3 = 136.2

#converts from degrees to radians
def degToRad(deg):
    return deg*(np.pi/180)

#the function that does the calculations
def jacobian(joint_angles, joint_velocities):

    J = np.array([[(-a3*np.sin(degToRad(joint_angles[0]))*np.cos(degToRad(joint_angles[1]+joint_angles[2]))-a2*np.sin(degToRad(joint_angles[0]))*np.cos(degToRad(joint_angles[1]))),
                        (-a3*np.cos(degToRad(joint_angles[0]))*np.sin(degToRad(joint_angles[1]+joint_angles[2]))-a2*np.cos(degToRad(joint_angles[0]))*np.sin(degToRad(joint_angles[1]))),
                        (-a3*np.cos(degToRad(joint_angles[0]))*np.sin(degToRad(joint_angles[1]+joint_angles[2])))],
                [(-a3*np.cos(degToRad(joint_angles[0]))*np.cos(degToRad(joint_angles[1]+joint_angles[2]))+a2*np.cos(degToRad(joint_angles[0]))*np.cos(degToRad(joint_angles[1]))),
                        (-a3*np.sin(degToRad(joint_angles[0]))*np.sin(degToRad(joint_angles[1]+joint_angles[2]))-a2*np.sin(degToRad(joint_angles[0]))*np.sin(degToRad(joint_angles[1]))),
                        (-a3*np.sin(degToRad(joint_angles[0]))*np.sin(degToRad(joint_angles[1]+joint_angles[2])))],
                [0,
                (-a3*np.cos(degToRad(joint_angles[1]+joint_angles[2]))-a2*np.cos(degToRad(joint_angles[1]))),
                (-a3*np.cos(degToRad(joint_angles[1]+joint_angles[2])))]])

    q = np.array([[joint_velocities[0]],
                    [joint_velocities[1]],
                    [joint_velocities[2]]])


    return J@q