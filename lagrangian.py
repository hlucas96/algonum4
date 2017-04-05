def elastic_force(u, u0, k):
    return [[-k * (u[0] - u0[0])], [-k* (u[1] - u0[1])]]

def J_elastic(u , u0, k):
    return [[-k], [0]
            [0], [-k]]

def centrifugal_force(u, u0, k):
    res = [[0], [0]]
    for i in range (2):
        res[i][0] = -k * (u[i] - u0[i])/((u[0] - u0[0])**2 +(u[1] - u0[1])**2)**(3/2)
    return res

def J_centrifugal_force(u , u0, k):
    denominateur = ((u[0] - u0[0])**2 + (u[1] - u0[1])**2)**(5/2)
    return [[k*(2((u[0] - u0[0])**2 - (u[1] - u0[1])**2))/denominateur], [3*k*(u[0] - u0[0])*(u[1] - u0[1])/denominateur]
            [3*k*(u[0] - u0[0])*(u[1] - u0[1])/denominateur], [k*(2((u[1] - u0[1])**2 - (u[0] - u0[0])**2))/denominateur]]

def gravitational_force(u, u0, k):
    
