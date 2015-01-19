using Distributions 

function normalize(arr)
  arr_min = minimum(arr)
  arr_max = maximum(arr)
  rng = arr_max - arr_min
  1 - ((arr_max - arr) / rng)
end

function gen_one_fbm(dim_len)
  times = 1:(dim_len+1)
  gamma = zeros((dim_len, dim_len))
  h = 0.8
  double_h = h * 2
  for i in 1:(dim_len)
    for j in 1:(dim_len)
      gamma[i, j] = (i ^ (double_h) + j ^ (double_h) - (abs(j - i) ^ double_h)) / 2 ## right indices?
    end
  end
  sigma = chol(gamma)
  vec = rand(Normal(), dim_len)
  u = *(sigma, vec)
  u = normalize(u)
  u
end

function gen_fbms(num=300)
  dim_len = 200
  fbms = [gen_one_fbm(dim_len) for x in 1:num]
end

genned = gen_fbms()
f = open("genned_fbms.jld", "w")
serialize(f, genned)

