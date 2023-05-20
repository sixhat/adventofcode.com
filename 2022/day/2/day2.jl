# https://adventofcode.com/2022/day/2

dStrategy = Dict("X" => 1, "Y" => 2, "Z" => 3)
dOpponent = Dict("A" => 1, "B" => 2, "C" => 3)
sSymbol = ["A", "B", "C"]

iSoma = 0
iSomaPart2 = 0

for line in eachline("input.data")
  asRound = split(line)

  # iRound can be 0, 1, 2, 
  # p2 wins when iRound = 1, ties for 0 and looses for 2.
  iRound = (dStrategy[asRound[2]] - dOpponent[asRound[1]] + 3) % 3

  # Part 1 - Just sum your points
  iSoma += dStrategy[asRound[2]] # Always get your strategy points
  if iRound == 0
    global iSoma += 3
  elseif iRound == 1
    global iSoma += 6
  end

  # Part 2 - Get the positon of your opponent and get the Position of your Elf to make it do the action. 
  if asRound[2] == "X" # Loose -> rotate 2 symbols
    iPos = 1 + (dOpponent[asRound[1]] + 1) % 3
    global iSomaPart2 += dOpponent[sSymbol[iPos]]
  elseif asRound[2] == "Y" # Draw -> same symbol
    global iSomaPart2 += dOpponent[asRound[1]] + 3
  elseif asRound[2] == "Z" # Win -> rotate 1 symbol
    iPos = 1 + dOpponent[asRound[1]] % 3
    global iSomaPart2 += dOpponent[sSymbol[iPos]] + 6
  end
end

# Part 1 
println(iSoma)
# Part 2 X is to loose, Y is to draw, Z is to win
println(iSomaPart2)