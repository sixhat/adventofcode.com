# https://adventofcode.com/2022/day/4
# The description of part 1 clearly points to "issubset, intersect" from Sets. 

function day4()
  lines = readlines("input.data")
  iTotal = 0
  iTotal2 = 0
  for line in lines
    sRanges = split(line, ",")
    sLeft = split(sRanges[1], "-")
    sRight = split(sRanges[2], "-")
    iLeftLo = parse(Int, sLeft[1])
    iLeftHi = parse(Int, sLeft[2])
    iRightLo = parse(Int, sRight[1])
    iRigthHi = parse(Int, sRight[2])
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