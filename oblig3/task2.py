from sympy import symbols, Matrix, pi, sin, cos, eye, pretty_print, simplify

mass = [0.3833, 0.2724, 0.1406]
L = [100.9, 222.1, 136.2]

theta1, theta2, theta3 = symbols('theta1 theta2 theta3')
L1, L2, L3 = symbols('L1 L2 L3')
gT = Matrix([[0,0,9.81]])
# uses the last column in the homogenious tranformations from assignment 2 (and shortened some of the expressions), and devided by 2 because the masses are in th emiddle of the link
r1 = Matrix([[[0],
              [0],
              [L[0]/2]]])
r2 = Matrix([[L[1]/2*cos(theta1)*cos(theta2)],
            [L[1]/2*cos(theta2)*sin(theta1)],
            [L[1]/2*sin(theta2)+L[1]]])

r3 = Matrix([[L[2]/2*cos(theta1)*cos(theta2+theta3)+L[1]*cos(theta1)*cos(theta2)],
             [L[2]/2*sin(theta1)*cos(theta2+theta3)+L[1]*sin(theta1)*cos(theta2)],
             [L[2]/2*sin(theta2+theta3)+L[1]*sin(theta2)+L[0]]])
r = [r1, r2, r3]

def degToRad(deg):
    return deg*(pi/180)

def rot_z(theta):
    mat = Matrix([[cos(theta), -sin(theta), 0, 0],
                    [sin(theta), cos(theta), 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]])
    return mat

R_M1 = Matrix([[1,0,0,0],
               [0,1,0,0],
               [0,0,1,0],
               [0,0,0,1]])
R_01 = Matrix([[1,0,0,0],
               [0,1,0,0],
               [0,0,1,L1/2],
               [0,0,0,1]])


def main():
    pretty_print(simplify(R_01))
    pretty_print(simplify(rot_z(theta1)))
    
main()