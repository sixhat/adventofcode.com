def day7():
    """
    --- Day 7: Laboratories ---
        https://github.com/sixhat/adventofcode.com/blob/main/2025/aoc2025-7-12.py
        https://adventofcode.com/2025/day/7

        A day of climbing up and down the Xmas Tree. Or is it down and up?
        The trick was to get the best representation of what was going on.
        A pencil and paper drawing helped to clear the mechanism of
        quantum tachyon manifolds. Post-modern physics is clearly kids play.

        tags: #AdventOfCode #python #pragrmming #xmas #coding
    """
    with open("day7.txt") as f:
        data = f.read().rstrip("\n").split("\n")

    # Sample data
    #     data = """.......S.......\n\
    # ...............
    # .......^.......
    # ...............
    # ......^.^......
    # ...............
    # .....^.^.^.....
    # ...............
    # ....^.^...^....
    # ...............
    # ...^.^...^.^...
    # ...............
    # ..^...^.....^..
    # ...............
    # .^.^.^.^.^...^.
    # ...............""".rstrip("\n").split("\n")

    # Find starting point
    data = [list(row) for row in data]
    beams = [[0, data[0].index("S")]]

    def print_tree(tree):
        """
        Print the XMAS-Tree
        """
        for line in tree:
            print("".join(line))

    line = 0
    splits = 0
    while line < len(data) - 1:
        new_beams = []
        for beam in beams:
            cell = data[beam[0] + 1][beam[1]]
            if cell == ".":
                data[beam[0] + 1][beam[1]] = "|"
                new_beams.append([beam[0] + 1, beam[1]])
            elif cell == "^":
                splits += 1
                data[beam[0] + 1][beam[1] - 1] = "|"
                data[beam[0] + 1][beam[1] + 1] = "|"
                new_beams.append([beam[0] + 1, beam[1] - 1])
                new_beams.append([beam[0] + 1, beam[1] + 1])
        beams = new_beams
        line += 1
    print_tree(data)
    print("Part 1:", splits)

    # Part 2
    #
    # We have the tree filled with lines. Maybe if we start on the bottom
    # this time we can trace our ways back and count the number of possibilities

    # Create a Zeros Matrix with the last line filled with 1s for "|"
    soma = []
    for i in range(len(data)):
        soma.append([0 for z in range(len(data[line]))])
    for i in range(len(data[line])):
        if data[line][i] == "|":
            soma[line][i] = 1

    # Let's climb the up the tree until we find a shooting Star
    while line >= 0:
        for i in range(len(data[line])):
            if data[line][i] == "|" and line < len(data)-1:
                y = line + 1 
                if data[y][i] == "^":
                    soma[line][i] += soma[y][i - 1] if i > 0 else 0
                    soma[line][i] += soma[y][i + 1] if i < len(data[line]) - 1 else 0
                else:
                    soma[line][i] += soma[y][i]
            if data[line][i] == "S":
                print("Part 2:", soma[line + 1][i])
        line -= 1


day7()
