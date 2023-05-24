# https://adventofcode.com/2022/day/8/
# This is interesting to parse the input data into a numerical matrix 
# using DelimitedFiles could be a solution if the data was space separated
# This solution is a bit of a Hack. Not proud of it. 


function day8()
  # lines = readlines("input_small.data")
  lines = readlines("input.data")

  d = length(lines)
  m = zeros(Int8, d, d)
  # Convert text to matrix.
  i = 1
  for line in lines
    j = 1
    for l in line
      m[i, j] = parse(Int, l)
      j += 1
    end
    i += 1
  end

  v = ones(Int8, d, d) # sets 1 for visibilty
  v = -1 * v


  for i = 2:(d-1)
    for j = 1:d
      if m[i, j] > v[i, 1]
        v[i, 1] = m[i, j]
        v[i, j] = v[i, 1]
      end
    end
    for j = (d):-1:1
      if m[i, j] > v[i, d]
        v[i, d] = m[i, j]
        v[i, j] = v[i, d]
      end
    end
  end

  # Transposing the Matrices we can then apply the same process
  m = m'
  v = v'

  for i = 2:(d-1)
    for j = 1:d
      if m[i, j] > v[i, 1]
        v[i, 1] = m[i, j]
        v[i, j] = v[i, 1]
      end
    end
    for j = (d):-1:1
      if m[i, j] > v[i, d]
        v[i, d] = m[i, j]
        v[i, j] = v[i, d]
      end
    end
  end

  # The 4 corners need to be included. 
  println("Part 1: ", length(v[v.>-1]) + 4)

  ## PART 2
  m = m'
  v = zeros(d, d)
  for i = 2:(d-1)
    for j = 2:(d-1)
      # walk 1 check if you can continue (do 4 times)
      west = 0
      while true
        west += 1
        if m[i, j-west] >= m[i, j] || (j - west) == 1
          break
        end
      end

      east = 0
      while true
        east += 1
        if m[i, j+east] >= m[i, j] || (j + east) == d
          break
        end
      end

      south = 0
      while true
        south += 1
        if m[i+south, j] >= m[i, j] || (i + south) == d
          break
        end
      end

      north = 0
      while true
        north += 1
        if m[i-north, j] >= m[i, j] || (i - north) == 1
          break
        end
      end

      v[i, j] = north * south * east * west
    end
  end
  print("Part 2: ", maximum(v))
end

day8()
