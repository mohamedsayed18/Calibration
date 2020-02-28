import numpy as np

def Tx(a):
    h = np.zeros((4,4))
    h[0,3] = a
    return h


def Ty(a):
    h = np.zeros((4,4))
    h[1,3] = a
    return h


def Tz(a):
    h = np.zeros((4,4))
    h[2,3] = a
    return h


def Rx (a):
    h = np.zeros((4,4))
    h[0,0] = 1
    h[1,1] = np.cos(a)
    h[1,2] = -np.sin(a)
    h[2,1] = np.sin(a)
    h[2,2] = np.cos(a)
    return h


def Ry (a):
    h = np.zeros((4,4))
    h[0,0] = np.cos(a)
    h[1,1] = 1
    h[0,2] = np.sin(a)
    h[2,0] = -np.sin(a)
    h[2,2] = np.cos(a)
    return h


def Rz(a):
    h = np.zeros((4,4))
    h[0,0] = np.cos(a)
    h[0,1] = -np.sin(a)
    h[1,0] = np.sin(a)
    h[1,1] = np.cos(a)
    h[2,2] = 1
    return h


def drx(a):
    h = np.zeros((4, 4))
    h[1,1]= -np.sin(a)
    h[1,2]= -np.cos(a)
    h[2,1] = np.cos(a)
    h[2,2] = np.sin(a)
    return h


def dry(a):
    h = np.zeros((4, 4))
    h[0,0]= -np.sin(a)
    h[0,2]= np.cos(a)
    h[2,1] = -np.cos(a)
    h[2,2] = -np.sin(a)
    return h


def drz(a):
    h = np.zeros((4, 4))
    h[0,0]= -np.sin(a)
    h[0,2]= -np.cos(a)
    h[1,0] = np.cos(a)
    h[1,1] = -np.sin(a)
    return h


def dtx(a):
    h = np.zeros((4, 4))
    h[0:3] = 1;
    return h


def dty(a):
    h = np.zeros((4, 4))
    h[1:3] = 1;
    return h


def dtz(a):
    h = np.zeros((4, 4))
    h[2:3] = 1;
    return h