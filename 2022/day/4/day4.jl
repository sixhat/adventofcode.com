# https://adventofcode.com/2022/day/4
# The problem clearly points to "issubset, intersect" from Sets. 
# The solution uses a regex (could go with splits, but no fun there, right?)

function day4()
  lines = readlines("input.data")
  iTotal = 0
  iTotal2 = 0
  for line in lines
    re = r"(\d+)-(\d+),(\d+)-(\d+)"
    reMatch = match(re, line)
    iLeftLo = parse(Int, reMatch[1])
    iLeftHi = parse(Int, reMatch[2])
    iRightLo = parse(Int, reMatch[3])
    iRigthHi = parse(Int, reMatch[4])
    # Create the two interavals as Sets.
    sL = Set(iLeftLo:iLeftHi)
    sR = Set(iRightLo:iRigthHi)
    # part 1
    if issubset(sL, sR) || issubset(sR, sL)
      iTotal += 1
    end
    # part 2
    if length(intersect(sL, sR)) > 0
      iTotal2 += 1
    end
  end
  return (iTotal, iTotal2)
end

println(day4());