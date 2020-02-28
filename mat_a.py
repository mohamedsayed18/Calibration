import numpy as np

from Jac_theta import jac_theta


def mat_a(q, force, param):
    j = jac_theta(q, param)
    # get the first three rows
    j = j[0:3, :]
    #print(j.shape)
    a = np.zeros((3,3))
    #print(force[:3,:].shape)
    for i in range(3):
        j1 = np.reshape(j[:, i], (3,1))
        t = j1 @ j1.T @ force[:3, :]
        a[:,i] = t.T
        #print(t)
    return a


"""
#test
q = [2, 2, 2]
param = [5, 5, 5, 5]
f = np.array([1,1,1,1,1,1])
f = f[:, np.newaxis]
#print(f.shape)
A = mat_a(q, f, param)
print(A)
"""