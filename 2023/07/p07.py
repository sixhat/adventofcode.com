import os
import functools

input = "demo"
input = "input"

part_b = False
cardsb = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def sort_joker(a, b):
    ia = cardsb.index(a[1])
    ib = cardsb.index(b[1])
    na = a[0]
    nb = b[0]
    if ia == 12:
        return +1
    if ib == 12:
        return -1

    if na != nb:
        return nb - na
    return ia - ib


def bump_joker_to_highest_type(a):
    ca = {}
    for c in range(5):
        if a[0][c] not in ca.keys():
            ca[a[0][c]] = 1
        else:
            ca[a[0][c]] += 1
    sa = [(e, k) for k, e in ca.items()]
    sa.sort(key=functools.cmp_to_key(sort_joker))
    kc = sa[0][1]
    if kc == "J":
        kc = "A"
    return a[0].replace("J", kc)


def sort_cards(a, b):
    cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    if part_b:
        cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    # if the sets are dif.
    s1 = a[0]
    s2 = b[0]
    if part_b:
        s1 = bump_joker_to_highest_type(a)
        s2 = bump_joker_to_highest_type(b)
    sa = len(set(s1))
    sb = len(set(s2))
    if sa != sb:
        return sb - sa

    # if the sets are equal but the types are dif.
    ca = {}
    cb = {}
    for c in range(5):
        if s1[c] not in ca.keys():
            ca[s1[c]] = 1
        else:
            ca[s1[c]] += 1

        if s2[c] not in cb.keys():
            cb[s2[c]] = 1
        else:
            cb[s2[c]] += 1
    ma = max(ca.values())
    mb = max(cb.values())
    if ma != mb:
        return ma - mb

    # if types are equal higher card is different
    for c in range(0, 5):
        if cards.index(a[0][c]) != cards.index(b[0][c]):
            return cards.index(b[0][c]) - cards.index(a[0][c])

    return 0  # otherwise the hands are the same.


def parte_a(data):
    total = 0
    hands = []
    for l in data:
        a = l.split()
        hands.append([a[0], int(a[1])])

    hands.sort(key=functools.cmp_to_key(sort_cards))

    for i, h in enumerate(hands):
        total += (i + 1) * h[1]

    print("-- Total parte A:\t", total)


def parte_b(data):
    global part_b
    part_b = True
    total = 0
    hands = []
    for l in data:
        a = l.split()
        hands.append([a[0], int(a[1])])

    hands.sort(key=functools.cmp_to_key(sort_cards))

    for i, h in enumerate(hands):
        total += (i + 1) * h[1]
    print("-- Total parte B:\t", total)


data: list[str] = (
    open(os.path.dirname(os.path.realpath(__file__)) + f"/{input}", "r")
    .read()
    .strip()
    .split("\n")
)


parte_a(data)
parte_b(data)
