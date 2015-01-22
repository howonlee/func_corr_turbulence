import numpy as np
import scipy.sparse as sci_sp
import networkx as nx

def make_net(fname="turb.dat"):
    dat = []
    with open(fname, "r") as net_file:
        dat = map(int, net_file.read().split())
    return dat

def save_retmap(vals, num_points=1000, cutoff=900):
    ret_mat = np.zeros((num_points, num_points))
    #probably a vectorized way to do it
    for x in xrange(num_points):
        for y in xrange(num_points):
            ret_mat[x,y] = abs(vals[x] - vals[y])
    ret_mat = np.logical_not(ret_mat > cutoff)
    net = nx.from_numpy_matrix(ret_mat)
    nx.write_edgelist(net, "turb.edgelist", data=False)

def load_graph(fname="turb.edgelist"):
    return nx.read_edgelist(fname)

if __name__ == "__main__":
    save_retmap(make_net())
