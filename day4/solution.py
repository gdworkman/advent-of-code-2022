import re

with open("input.txt") as f:
    input = f.read().splitlines()

input = [list(map(int, re.split(',|-', str))) for str in input]

tot1 =tot2 = 0

for x in input:
    if (
        (x[0] <= x[2] and x[1] >= x[3]) or
        (x[0] >= x[2] and x[1] <= x[3])
    ):
        tot1 +=1

    if x[1] >= x[2] and x[0] <= x[3]:
        tot2 += 1

print(f"Part 1: {tot1}")
print(f"Part 2: {tot2}")