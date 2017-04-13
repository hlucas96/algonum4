from newton import *

def centrifugal_force(u0, k):
    return lambda u : np.array([[k * (u[0][0] - u0[0][0])],
                                [k* (u[1][0] - u0[1][0])]])

def J_centrifugal_force(u0, k):
    return lambda u : np.array([[k, 0],
                                [0, k]])

def gravitational_force(u0, k):
    return lambda u : np.array([[-k * (u[0][0] - u0[0][0])/((u[0][0] - u0[0][0])**2 +(u[1][0] - u0[1][0])**2)**(3/2) ],
                                [-k * (u[1][0] - u0[1][0])/((u[0][0] - u0[0][0])**2 +(u[1][0] - u0[1][0])**2)**(3/2)]])

def J_gravitational_force(u0, k):
    return lambda u : np.array([[k*( 2*(u[0][0] - u0[0][0])**2 - (u[1][0] - u0[1][0])**2 ) / ( (u[0][0] - u0[0][0])**2 + (u[1][0] - u0[1][0])**2)**(5/2),
                                 3*k*(u[0][0] - u0[0][0])*(u[1][0] - u0[1][0]) / ( ((u[0][0] - u0[0][0])**2 + (u[1][0] - u0[1][0])**2)**(5/2))],
                                [3*k*(u[0][0] - u0[0][0])*(u[1][0] - u0[1][0])/((u[0][0] - u0[0][0])**2 + (u[1][0] - u0[1][0])**2)**(5/2),
                                 k*( 2*(u[1][0] - u0[1][0])**2 - (u[0][0] - u0[0][0])**2)/((u[0][0] - u0[0][0])**2 + (u[1][0] - u0[1][0])**2)**(5/2)]])


def sum_fct_force(U):

    k1 = 1
    u01 = np.array([[0], [0]])
    g1 = gravitational_force(u01, k1)
    Jg1 = J_gravitational_force(u01, k1)

    k2 = 0.01
    u02 = np.array([[1], [0]])
    g2 = gravitational_force(u02, k2)
    Jg2 = J_gravitational_force(u02, k2)

    k = 1
    u03 = np.array([[0.01/1.01], [0]])
    c1 = centrifugal_force(u03, k)
    Jc1 = J_centrifugal_force(u03, k)

    f = lambda U : (g1(U) + g2(U) + c1(U))
    J = lambda U: (Jg1(U) + Jg2(U) + Jc1(U))
    return f, J
    
def Newton_example(U):

    f, J = sum_fct_force(U)
    
    return Newton_Raphson(f, J, U, 10000, 0.01)
    

def test__fct_force():
    U = np.array([[1.5], [0]])
    f, J = sum_fct_force(U)

    print("f(U) = ")
    print (f(U))
    print("df(U) = ")
    print (J(U))

    print("Le point d'equilibre est : ")
    print(Newton_example(U))

test__fct_force()
