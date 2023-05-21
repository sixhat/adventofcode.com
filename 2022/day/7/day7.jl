# https://adventofcode.com/2022/day/7
# I'm scared of this one. It is basically a DAG (if there are no symlinks)
# Probably this can be computed with a Stack. 
# Note:
# - BAD: Used the name of the folder as key forgetting that same name can exist in different locations GOOD: usef full path.
# - Still not very confortable using Dicts in Julia. Found `findmin` but don't know why `min` doesn't work.
# - Used a stack but this model doesn't consider that the user can repeat going into the same folder several times. 
# - There might be a simpler way to solve this (namely with a DAG or recursion)
using DataStructures

function day7()
  dDirs = Dict{String,Int}()
  sPath = Stack{String}()

  lines = readlines("input.data")
  for line in lines
    tok = split(line)
    # Match 1st token to one of
    if tok[1] == "\$"
      if tok[2] == "cd"
        if tok[3] == ".."
          fp0 = join(sPath, ":")
          pop!(sPath)
          fp = join(sPath, ":")
          dDirs[fp] += dDirs[fp0]
        else
          push!(sPath, tok[3])
          fp = join(sPath, ":")
          push!(dDirs, fp => 0)
        end
      end
    elseif tok[1] == "dir"
    else
      # 1st token is a number
      iSize = parse(Int, tok[1])
      dDirs[join(sPath, ":")] += iSize
    end
    #println(join(sPath, ":"))
  end
  # Accumulate the path
  while length(sPath) > 1
    outOff = join(sPath, ":")
    pop!(sPath)
    dDirs[join(sPath, ":")] += dDirs[outOff]
  end


  println(join(sPath, ":"))
  sub100 = filter(p -> last(p) <= 100000, dDirs)
  print("Part 1: ")
  println(sum(values(sub100)))

  iFree = 70000000 - dDirs["/"]
  target = 30000000
  println("Total Size : ", dDirs["/"])
  println("Total Free : ", iFree)
  iNeeded = target - iFree
  println("Total Needed : ", iNeeded)
  vals = filter(p -> last(p) > iNeeded, dDirs)
  println("Part 2: ", findmin(vals))
end

day7()