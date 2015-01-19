import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import numpy.linalg as np_lin
import numpy.random as npr

def calc_autocorrelation(fbms):
    """
    Understand and then calculate the autocorrelation
    """
    pass

def normalize(arr):
    arr_min = np.min(arr)
    arr_max = np.max(arr)
    rng = arr_max - arr_min
    return 1 - ((arr_max - arr) / rng)

def gen_one_fbm(dim_len=2000):
    times = range(1, dim_len + 1)
    gamma = np.zeros((dim_len, dim_len))
    h = 0.8
    double_h = h * 2
    for i in times:
        for j in times:
            gamma[i-1, j-1] = (i ** (double_h) + j ** (double_h) - (abs(j - i) ** double_h)) / 2
    sigma = np_lin.cholesky(gamma)
    vec = npr.normal(size=(dim_len,))
    u = np.dot(sigma, vec)
    u = normalize(u)
    return u

def gen_fbms(num=3000):
    dim_len = 2000
    fbms = np.zeros(dim_len)
    for x in xrange(num):
        fbms = np.hstack((fbms, gen_one_fbm(dim_len)))
        print x
    return fbms

if __name__ == "__main__":
    print gen_fbms()
    pass
