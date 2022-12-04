# Advent of Code Day 3 2022
# Graeme Workman


def prio(c):
    if c.isupper():
        return ord(c) - 38
    else:
        return ord(c) - 96

with open("input.txt") as f:
    input = f.read().splitlines()

input_grouped = zip(input[::3], input[1::3], input[2::3])
tot1 = tot2 = 0

for group in input_grouped:
    badge = (set(group[0]) & set(group[1]) & set(group[2])).pop()
    tot2 += prio(badge)
    
    for pack in group:
        c1, c2 = pack[:len(pack)//2], pack[len(pack)//2:]
        common = (set(c1) & set(c2)).pop()
        tot1 += prio(common)
    

print(f"Part 1: {tot1}")
print(f"Part 2: {tot2}")

