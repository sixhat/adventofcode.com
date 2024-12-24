wires, logic = open(0).read().split("\n\n")
wires = wires.split("\n")

wire = {}
for line in wires:
    wire[line[0:3]] = int(line[-1])

logic = logic.split("\n")

repeat = True
while repeat:
    repeat = False
    for line in logic:
        a, op, b, _, c = line.split()
        if a in wire.keys() and b in wire.keys():
            if op == "AND":
                wire[c] = wire[a] * wire[b]
            elif op == "OR":
                wire[c] = 0 if wire[a] + wire[b] == 0 else 1
            elif op == "XOR":
                wire[c] = 0 if wire[a] == wire[b] else 1
        else:
            repeat = True

final = sorted([w for w in wire if w[0] == "z"])
number = 0
for e in final:
    p = int(e[-2:])
    number = number + wire[e] * (2**p)

print(number)
