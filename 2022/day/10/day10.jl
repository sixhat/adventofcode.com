# https://adventofcode.com/2022/day/10
# setup
#
lines = readlines("input.data")

function run(lines)
  cycles = 0
  xR = 1
  strength = 0
  for line in lines
    el = split(line)
    for i = 1:length(el)
      if cycles % 40 in [xR - 1, xR, xR + 1]
        print("#")
      else
        print(" ")
      end

      cycles += 1

      if cycles in [20, 60, 100, 140, 180, 220]
        strength += cycles * xR
      end

      if cycles in [40, 80, 120, 160, 200, 240]
        println("")
      end
    end
    if length(el) == 2
      xR += parse(Int, el[2])
    end
    # println(cycles, "\t", xR, "\t", line)
  end
  strength
end

println("Part 1: ", run(lines))
