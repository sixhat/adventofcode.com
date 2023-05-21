#= https://adventofcode.com/2022/day/6
Is this is a Queue of size 3 or a Set? Again Sets are best.
=#
using DataStructures

function marker(n, line)
  for i = n:length(line)
    q = Set{Char}()
    for j = 0:(n-1)
      push!(q, line[i-j])
    end
    if length(q) == n
      println("Marker ", n, " => ", i)
      break
    end
  end
end

function day6()
  line = readline("input.data")
  marker(4, line)
  marker(14, line)
end

day6()