"""the main code for calibration"""
import numpy as np
import random

from deflection import deflection
from mat_a import mat_a

links = [1, 1, 1, 1]
exp = 3   # No. of experiments
forces = np.zeros((6, exp))
poses = np.zeros((3, exp))
defi = []

s1 = np.zeros((3,3))
s2 = np.zeros((3,3))

for i in range(exp):
    # generate random forces
    force = np.zeros((6,1))
    force[:3, 0] = np.asarray(random.sample(range(1, 100), 3))
    forces[:, i] = force.T

    # generate random joint values
    q = np.zeros((3,1))
    q = random.sample(range(1, 10), 3)
    poses[:,i] = q

    # calculate displacement for these positions and forces
    dt, dq = deflection(q, force, links)
    defi.append(np.linalg.norm(dt))

    dt = dt[:3,0]
    A = mat_a(q, force, links)

    s1 = s1 + A.T @ A
    s2 = s2 + A.T * dt


# compliance
#k = np.linalg.lstsq(s1,s2)[0]
k = np.linalg.lstsq(s1, s2, rcond=-1)

print(dt.shape)