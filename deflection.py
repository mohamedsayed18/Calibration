import numpy as np

from Jac_theta import jac_theta
from k_full import k_full


def deflection(q,force,param):
    """calculate the deflection and dq"""
    j = jac_theta(q, param)
    k = k_full()
    dq, _, _, _ = np.linalg.lstsq(k,(j.T @ force), rcond=-1)
    dt = j @ dq
    return dt, dq