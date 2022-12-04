# Advent of Code Day 2 2022
# Graeme Workman

combos1 = {
    "A": {"X": 4, "Y": 8, "Z": 3},
    "B": {"X": 1, "Y": 5, "Z": 9},
    "C": {"X": 7, "Y": 2, "Z": 6}
}

combos2 = {
    "A": {"X": 3, "Y": 4, "Z": 8},
    "B": {"X": 1, "Y": 5, "Z": 9},
    "C": {"X": 2, "Y": 6, "Z": 7}
}


with open("input.txt") as f:
    input = f.read().splitlines()

tot1 = tot2 = 0

for line in input:
    tot1 += combos1[line[0]][line[-1]]
    tot2 += combos2[line[0]][line[-1]]

print(f"Part 1: {tot1}")
print(f"Part 2: {tot2}")