#= 
https://adventofcode.com/2022/day/5
input.data might need to be manipulated into 2 separate files. One defining
the initial stacks and the second defining the commands. Here I transposed the 
initial stacks definition outside.
Part 1 is a simple stack manipulation. We have N stacks and push and pop 
according to the the rules parsed in the input.data 
The commands will easily parsed with a regex.

-- Bodged code. Need to rewrite this in an elegant way.
=#

using DataStructures

# We need 9 stacks (as per input.data)
stacks = []
for i in 1:9
	push!(stacks, Stack{Char}())
end

reCommand = r"move (\d+) from (\d+) to (\d+)"
lines = readlines("input.data")

stack = 0
for line in lines[1:9]
  global stack += 1
  for l in line
    println(stacks[stack])
    push!(stacks[stack], l)
  end
end

for line in lines[11:length(lines)]
	println(line)
  reMatch = match(reCommand, line)
	println(reMatch)
	iHowMany = parse(Int,reMatch[1])
  iFrom = parse(Int,reMatch[2])
  iTo = parse(Int,reMatch[3])

	#= # Part 1 - Uncomment this block for part  part 1
	for i in 1:iHowMany
		push!(stacks[iTo], pop!(stacks[iFrom]))
	end
	# end of part 1 =#

	# Part 2 - Needs a temporary stack to reverse the order / uncoment for part 2
	tempStack = Stack{Char}() # For part 2
	for i in 1:iHowMany
		push!(tempStack, pop!(stacks[iFrom]))
	end
	for i in 1:iHowMany
		push!(stacks[iTo], pop!(tempStack))
	end
	# end of part 2

end

for i in 1:9
	print(pop!(stacks[i]))
end

