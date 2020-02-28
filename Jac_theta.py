import numpy as np

from rot_trans import *


def jac_theta(q, param):
    """get the theta jacobian
    Tz(l1). Rz(q1) . Tz(l2) . Tz(q2) . Tx(l3) . Tx(q3) . Tx(l4)
    """
    j = np.zeros((6, 3))
    l1, l2, l3, l4 = param

    t = Tz(l1) @ Rz(q[0]) @ drz(0) @ Tz(l2) @ Tz(q[1]) @ Tx(l3) @ Tx(q[2]) @ Tx(l4)
    j[:, 0] = np.array([t[0:3, 3][0],t[0:3, 3][1],t[0:3, 3][2], t[2,1], t[0,2], t[1,0]])
    t = Tz(l1) @ Rz(q[0]) @ Tz(l2) @ Tz(q[1]) @ dtz(0) @ Tx(l3) @ Tx(q[2]) @ Tx(l4)
    j[:, 1] = np.array([t[0:3, 3][0], t[0:3, 3][1], t[0:3, 3][2], t[2, 1], t[0, 2], t[1, 0]])
    t = Tz(l1) @ Rz(q[0]) @ Tz(l2) @ Tz(q[1]) @ Tx(l3) @ Tx(q[2]) @ dtx(0) @ Tx(l4)
    j[:, 2] = np.array([t[0:3, 3][0], t[0:3, 3][1], t[0:3, 3][2], t[2, 1], t[0, 2], t[1, 0]])
    return j


""""
#test
q = [2, 2, 2]
param = [5, 5, 5, 5]
e = jac_theta(q, param)
#x = drz(5)
print (e.shape)

#e = Tz(2)
#print(e.shape)
"""