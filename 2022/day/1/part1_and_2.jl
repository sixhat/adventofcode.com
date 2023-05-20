# Learning Julia using the Advent of code challenges:
# https://adventofcode.com/2022/day/1

suma = 0
all_sums = []

for line in eachline("input.data")
  if line == ""
		push!(all_sums, suma)
    global suma = 0
  else
    global suma = suma + parse(Int, line)
  end
end

sort!(all_sums, rev=true)
println("Part 1 ", all_sums[1])
println("Part 2 ",sum(all_sums[1:3]))
