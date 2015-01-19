using Distributions
using PyPlot

f = open("genned_fbms.jld", "r")
genned = deserialize(f)
plt.plot(genned[1])
plt.savefig("genned")
