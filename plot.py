import numpy as np
import matplotlib.pyplot as plt
import h5py

f = h5py.File("isotropic1024fine.h5", "r")
total_array = np.array([0,0,0])
for name in f:
    last_arr = np.squeeze(f[name][...])
    print last_arr
    if last_arr.shape == (3,):
        total_array = np.vstack((total_array, last_arr))
print "====="
print total_array
one_col = total_array[:,1]
plt.plot(one_col)
plt.show()
