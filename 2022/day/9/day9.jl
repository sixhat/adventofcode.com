# https://adventofcode.com/2022/day/9/
# Can I use a struct?
# Might not need the location if instead I just use tupples
# I went with structs imagining that I'd do interesting things with them, but in the end Location became a pain to use. Also took me long time to find a bug in part2 and with that had to write a lot of "tooling" to debug the issue. Anyhow, Elves continue. 

struct Location # (x,y) atenção às matrizes
  x::Int
  y::Int
end
dir = Dict("U" => Location(0, 1), "D" => Location(0, -1), "L" => Location(-1, 0), "R" => Location(1, 0))

struct Command
  direction::String
  steps::Int
  dir
end

function add(a::Location, b::Location)
  Location(a.x + b.x, a.y + b.y)
end
function sub(a::Location, b::Location)
  Location(a.x - b.x, a.y - b.y)
end
function dabs(a::Location)
  Location(abs(a.x), abs(a.y))
end
function div(a::Location, b::Location)
  if b.x == 0 
    return Location(0, a.y ÷ b.y)
  end
  if b.y == 0 
    return Location(a.x ÷  b.x, 0)
  end
  Location(a.x ÷  b.x, a.y ÷ b.y)
end
function dist(a::Location, b::Location)
  v = add(a, mul(b, -1))
  sqrt(v.x^2 + v.y^2)
end
function mul(a::Location, b::Int)
  Location(a.x * b, a.y * b)
end
function minmax(nodes)
  n = 0
  m = 0
  xx = [d.x for d in nodes]
  yy = [ d.y for d in nodes]

  n = minimum([minimum(xx), minimum(yy)])
  m = maximum([maximum(xx), maximum(yy)])

  Location(n,m)
end

function printNodes(nodes)
  a = minmax(nodes)
  d = a.y - a.x + 1
  m = zeros(Int, d, d)
  # println(a)
  # println(nodes)
  # XXX Agora é isto que não é genérico.
  
  for i = 10:-1:1
    n = nodes[i]
    i > 1 ? m[a.y-n.y+1, n.x-a.x+1] = i - 1 : m[a.y-n.y+1, n.x-a.x+1] = -1
  end

  for r = 1:size(m, 1)
    for c = 1:size(m, 2)
      if m[r, c] == 0
        print(".")
      elseif m[r, c] == -1
        print("H")
      else
        print(m[r, c])
      end
    end
    println()
  end
  println()
end

# This moves the Head perfectly. The problem is that the tail doesn't follow exactly the same rules.
# Also this doesn't create the path. So it might be necessary to run the commmand on the path. 
function run(c::Command, l::Location)
  add(l, dir[c.direction])
end


## Initicalization of variables and setup of commands
program = Command[]
pathHead::Array{Location} = []
pathTail::Array{Location} = []

lines = readlines("input.data")
# lines = readlines("input_small2.data")

for line in lines
  c, s = split(line)
  push!(program, Command(c, parse(Int, s), dir[c]))
end

head = Location(0, 0)
tail = Location(0, 0)
push!(pathHead, head)
push!(pathTail, tail)

## Run the program 

for c in program
  for i = 1:c.steps
    # The problem is the tail... 
    next = add(head, c.dir)

    if dist(tail, next) >= 2.0 # ou 1.5 
      tail = head
      push!(pathTail, tail)
    end
    head = next
    push!(pathHead, head)
  end
end
head
tail
pathHead
pathTail

# interested only in the set of unique elements (Using Sest)
println("All visited: ", length(pathTail))
println("Part 1: ", length(Set(pathTail)))



## Part 2 
# There must be another way to slove this starting from the head
# and going down the rope. Important for Part 2
# And keep track of all movements in a queue

let nodes::Array{Location} = [
    Location(0, 0),
    Location(0, 0),
    Location(0, 0),
    Location(0, 0),
    Location(0, 0),
    Location(0, 0),
    Location(0, 0),
    Location(0, 0),
    Location(0, 0),
    Location(0, 0)
  ]

  println("----------------------------------------------------")


  nNodes = length(nodes)
  pathTail2::Array{Location} = []
  # head run command
  
  for (ind,c) in pairs(program)
    println(ind,c)
    for i = 1:c.steps
      nodes[1] = add(nodes[1], c.dir)
      for i = 2:nNodes
        t = dist(nodes[i], nodes[i-1])
        if t >= 2
          dDir = sub(nodes[i-1], nodes[i]) 
          dDir = Location(sign(dDir.x), sign(dDir.y))
          nodes[i] = add(nodes[i], dDir)
        end
        i == nNodes && push!(pathTail2, nodes[i])
      end
    end
  end

  #pathTail2
  println("Part 2: ", length(Set(pathTail2))
end