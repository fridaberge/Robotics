#!/usr/bin/env python3

"""
Implementation of a PID controller.

Assignment 4, in3140
"""
import rospy
import math


class PID(object):
    def __init__(self):
        # Proportional constant
        self.p = 0.0
        # Integral constant
        self.i = 0.0
        # Integral accumulation variable
        self.integral = 0.0
        # Derivative constant
        self.d = 0.0
        # the integral time
        self.c = 0.0
        # Position error
        self.error = 0.0

    def __call__(self, desired_theta, current_theta, velocity_theta, dt):
        # TODO: Change which line is commented according to which part
        # you are testing in your code.
        #return self.P_ctrl(desired_theta, current_theta, dt)
        #return self.PD_ctrl(desired_theta, current_theta, velocity_theta, dt)
        #return self.PID_ctrl(desired_theta, current_theta, velocity_theta, dt)
        return self.PI_ctrl(desired_theta, current_theta, velocity_theta, dt)

    def P_ctrl(self, desired_theta, current_theta, dt):
        # TODO: Implement!
        # TIP: Use 'rospy.loginfo' to print output in ROS
        self.error = desired_theta-current_theta
        P = self.p*self.error
        return P

    def PD_ctrl(self, desired_theta, current_theta, velocity_theta, dt):
        # TODO: Implement!
        # TIP: Use 'rospy.loginfo' to print output in ROS
        self.error = desired_theta-current_theta
        P = self.p*self.error
        D = -self.d*velocity_theta
        u = P+D
        return u

    def PID_ctrl(self, desired_theta, current_theta, velocity_theta, dt):
        # TODO: Implement!
        # TIP: Use 'rospy.loginfo' to print output in ROS
        self.error = desired_theta-current_theta
        P = self.p*self.error
        I = self.i*self.integral*self.error*dt
        D = -self.d*velocity_theta
        u = P+I+D
        return u

    def PI_ctrl(self, desired_theta, current_theta, velocity_theta, dt):
        #Task4
        # TODO: Implement!
        # TIP: Use 'rospy.loginfo' to print output in ROS
        if(self.p == 0 and self.d == 0):
            Td = 0
        else:
            Td = self.d / self.p
        
        self.error = desired_theta-current_theta
        if(self.p == 0 and self.i == 0):
            Ti = float('inf')
        else:
            Ti = self.p / self.i
            
        exp = self.error+(self.error)/(Ti*dt)+self.error*Td*dt
        H = self.p*exp
        
        return H
