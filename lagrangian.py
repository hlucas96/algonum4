from newton import *

def centrifugal_force(u, u0, k):
    return np.array([[-k * (u[0][0] - u0[0][0])], [-k* (u[1][0] - u0[1][0])]])

def J_centrifugal_force(u, u0, k):
    return np.array([[-k, 0],
                    [0, -k]])

def gravitational_force(u, u0, k):
    res = np.array([[0], [0]])
    for i in range (2):
        res[i][0] = -k * (u[i][0] - u0[i][0])/((u[0][0] - u0[0][0])**2 +(u[1][0] - u0[1][0])**2)**(3/2)
    return res

def J_gravitational_force(u, u0, k):
    denominateur = ((u[0][0] - u0[0][0])**2 + (u[1][0] - u0[1][0])**2)**(5/2)
    return np.array([[k*(2*((u[0][0] - u0[0][0])**2 - (u[1][0] - u0[1][0])**2))/denominateur,
                    3*k*(u[0][0] - u0[0][0])*(u[1][0] - u0[1][0])/denominateur],
                    [3*k*(u[0][0] - u0[0][0])*(u[1][0] - u0[1][0])/denominateur,
                    k*(2*((u[1][0] - u0[1][0])**2 - (u[0][0] - u0[0][0])**2))/denominateur]])


def Newton_example(U):
    u0 = np.array([[0], [0]])
    k1 = 1
    u01 = np.array([[0], [0]])
    GF1 = gravitational_force(U, u01, k1)

    k2 = 0.01
    u02 = np.array([[1], [0]])
    GF2 = gravitational_force(U, u02, k2)

    k = 1
    u03 = np.array([[0], [0]])

    f = lambda U: gravitational_force(U, u01, k1) + gravitational_force(U, u02, k2) + centrifugal_force(U, u03, k)
    J = lambda U: J_gravitational_force(U, u01, k1) + J_gravitational_force(U, u02, k2) + J_centrifugal_force(U, u03, k)

    return Newton_Raphson_backtracking(f, J, U, 100, 0.01)

U = np.array([[1.5], [0]])
print(Newton_example(U))
