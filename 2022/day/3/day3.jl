# https://adventofcode.com/2022/day/3
# This solution takes advantage of Set operations (namely intersect)

lines = readlines("input.data")

# Part 1
iSoma = 0
for line in lines
  iMeio::Int = length(line) / 2
  sLeft = Set(line[1:iMeio])
  sRight = Set(line[iMeio+1:2*iMeio])
  lSet = intersect(sLeft, sRight)
  letter = Int(first(lSet))
  letter -= letter > 94 ? 96 : 38
  global iSoma += letter
end
println(iSoma)

# Part 2 (each elf group is made of 3 lines of strings)
iSoma2 = 0
for i in 1:3:length(lines)
  s1 = Set(lines[i])
  s2 = Set(lines[i+1])
  s3 = Set(lines[i+2])
  lSet = intersect(s1, s2, s3)
  letter = Int(first(lSet))
  letter -= letter > 94 ? 96 : 38
  global iSoma2 += letter
end
println(iSoma2)
