def transpose(d: list[str])-> list[str]:
    return ["".join(a) for a in list(zip(*d))]

def pprint(d: list[str]):
    print('\n'.join(d))
    print("")

def flip(d: list[str], hor=True)-> list[str]:
    if hor:
        out = ["".join(list(reversed(list(x)))) for x in d]
        return out
    return ["".join((list(x))) for x in rotccw(transpose(d))]

def rotcw(d: list[str])-> list[str]:
    return flip(transpose(d))

def rotccw(d: list[str])-> list[str]:
    return (transpose(flip(d)))


def rot180(d: list[str])-> list[str]:
    return(flip(flip(d, False)))
