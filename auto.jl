using Distributions

f = open("genned_fbms.jld", "r")
genned = deserialize(f)

function corr(first, second)
  ## correlation between two voxels
end

function automat(mat)
  ## whole autocorrelation matrix
end
