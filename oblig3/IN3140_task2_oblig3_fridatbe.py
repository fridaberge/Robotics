import numpy as np
from sympy import symbols, Matrix, pi, sin, cos, eye, pretty_print, zeros, shape, simplify, diag, diff
from sympy.physics.vector import ReferenceFrame, dynamicsymbols, time_derivative


mass = [0.3833, 0.2724, 0.1406]
theta1, theta2, theta3, tdot1, tdot2, tdot3, tdotdot1, tdotdot2, tdotdot3 = symbols('theta1 theta2 theta3 qdot1 qdot2 qdot3 qdotdot1 qdotdot2 qdotdot3')
L1, L2, L3 = symbols('L1 L2 L3')
thetas = Matrix([[theta1],
                 [theta2],
                 [theta3]])
I1x, I1y, I1z, I2x, I2y, I2z, I3x, I3y, I3z = symbols('I1x I1y I1z I2x I2y I2z I3x I3y I3z')
g = Matrix([[0],
            [0],
            [9.81]])
qdot = Matrix([[tdot1],
              [tdot2],
              [tdot3]])
qdotdot = Matrix([[tdotdot1],
                  [tdot2],
                  [tdot3]])

# uses the last column in the homogenious tranformations from assignment 2 (and shortened some of the expressions), and devided by 2 because the masses are in th emiddle of the link
r1 = Matrix([[0],
             [0],
             [L1/2]])

r2 = Matrix([[L2/2*cos(theta1)*cos(theta2)],
            [L2/2*cos(theta2)*sin(theta1)],
            [L2/2*sin(theta2)+L1]])

r3 = Matrix([[L3/2*cos(theta1)*cos(theta2+theta3)+L2*cos(theta1)*cos(theta2)],
             [L3/2*sin(theta1)*cos(theta2+theta3)+L2*sin(theta1)*cos(theta2)],
             [L3/2*sin(theta2+theta3)+L2*sin(theta2)+L1]])
r = [r1, r2, r3]

I1 = Matrix([[I1x, 0,0],
             [0, I1y, 0],
             [0,0,I1z]])
I2 = Matrix([[I2x, 0,0],
             [0, I2y, 0],
             [0,0,I2z]])
I3 = Matrix([[I3x, 0,0],
             [0, I3y, 0],
             [0,0,I3z]])
I = [I1, I2, I3]

Jv = Matrix([[-sin(theta1)*(L2*cos(theta2)+L3*cos(theta2+theta3)), -cos(theta1)*(L2*sin(theta2)+L3*sin(theta2+theta3)), -cos(theta1)*(L3*sin(theta2+theta3))],
             [cos(theta1)*(L2*cos(theta2)+L3*cos(theta2+theta3)), -sin(theta1)*(L2*sin(theta2)+L3*sin(theta2+theta3)), -sin(theta1)*(L3*sin(theta2+theta3))],
             [0, L2*cos(theta2)+L3*cos(theta2+theta3), L3*cos(theta2+theta3)]])

Jw = Matrix([[0,sin(theta1),sin(theta1)],
             [0,-cos(theta1), -cos(theta1)],
             [1,0,0]])

rot_z2 = Matrix([[cos(theta2), -sin(theta2), 0],
                [sin(theta2), cos(theta2), 0],
                [0, 0, 1]])
rot_z3 = Matrix([[cos(theta3), -sin(theta3), 0],
                [sin(theta3), cos(theta3), 0],
                [0, 0, 1]])
M1 = Matrix([[1,0,0],
             [0,1,0],
             [0,0,1]])
M2 = M1*rot_z2
M3 = M2*rot_z3

def pot():
    prod1 = mass[0]*g.T*r[0]
    prod2 = mass[1]*g.T*r[1]
    prod3 = mass[2]*g.T*r[2]
    return prod1+prod2+prod3

def kin():
    col1 = diag(1,0,0)
    col2 = diag(1,1,0)
    Jv1 = Jv.subs([(cos(theta2), 0), (cos(theta3), 0), (sin(theta2), 0),  (sin(theta3), 0), (cos(theta2+theta3), 0),  (sin(theta2+theta3), 0),  (L2, 0),  (L3, 0),  ])
    Jv2 = Jv.subs([(cos(theta3), 0), (sin(theta3), 0), (cos(theta2+theta3), 0),  (sin(theta2+theta3), 0),  (L3, 0)])
    Jv3 = Jv
    Jw1 = Jw.subs([(cos(theta2), 0), (cos(theta3), 0), (sin(theta2), 0),  (sin(theta3), 0), (cos(theta2+theta3), 0),  (sin(theta2+theta3), 0),  (L2, 0),  (L3, 0),  ])
    Jw2 = Jw.subs([(cos(theta3), 0), (sin(theta3), 0), (cos(theta2+theta3), 0),  (sin(theta2+theta3), 0),  (L3, 0)])
    Jw3 = Jw

    k1v = mass[0]*(Jv1*col1).T*Jv1*col1
    k1w = (Jw1*col1).T*M1*I1*M1.T*Jw1*col1
    k1 = k1v+k1w

    k2v = mass[1]*Jv2*col2.T*Jv2*col2
    k2w = (Jw2*col2).T*M2*I2*M2.T*Jw2*col2
    k2 = k2v+k2w

    k3v = mass[2]*Jv3*Jv3
    k3w = Jw3.T*M1*I1*M3.T*Jw3
    k3 = k3v+k3w

    return k1+k2+k3

def cor(D):
    C = zeros(3,3)
    for k in range(3):
        for j in range(3):
            for i in range(3):
                C[k,j] = (1/2)*(diff(D[k,j],thetas[i])+diff(D[k,i],thetas[j])-diff(D[i,j], thetas[k]))*qdot[i]
    return C

def tau(D,C,g):
    print(shape(D), shape(C), shape(g))
    tau = zeros(3,1)
    Dpart = D*qdotdot
    Cpart = C*qdot
    # print(shape(Dpart), shape(Cpart), shape(g))

    return Dpart+Cpart+g


def main():

    # # task 2a)
    # print("Potential energy:")
    # pretty_print(pot())

    # # task 2b)
    # print("Kinetic energy:")
    D = kin()
    K = (1/2)*qdot.T*(D)*qdot
    # pretty_print(K)

    # # task 2d)
    # print("g(q):")
    # pretty_print(g)
    # print("\nC(q,qdot):")
    C = cor(D)
    # pretty_print(C)

    # task 2e)
    t = tau(D,C,g)
    pretty_print(t)


main()