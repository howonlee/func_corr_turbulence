import matplotlib.pyplot as plt
import numpy as np

def return_map(vals, num_pts=1000):
    vals = vals[:num_pts]
    ret_mat = np.zeros((num_pts, num_pts))
    #probably a vectorized way to do it
    for x in xrange(num_pts):
        for y in xrange(num_pts):
            ret_mat[x,y] = abs(vals[x] - vals[y])
    plt.matshow(ret_mat)
    plt.show()
    plt.savefig("turb_retmap")

def binary_return_map(vals, num_pts=1000, cutoff=500):
    vals = vals[:num_pts]
    ret_mat = np.zeros((num_pts, num_pts))
    #probably a vectorized way to do it
    for x in xrange(num_pts):
        for y in xrange(num_pts):
            ret_mat[x,y] = abs(vals[x] - vals[y])
    ret_mat = np.logical_not(ret_mat > cutoff)
    plt.matshow(ret_mat)
    plt.show()
    plt.savefig("turb_binary_retmap")


if __name__ == "__main__":
    turb_data = []
    with open("turb.dat", "r") as turb_file:
        turb_data = map(int, turb_file.read().split())
    binary_return_map(turb_data)
