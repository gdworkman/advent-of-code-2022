# Advent of Code Day 1 2022
# Graeme Workman
import heapq

with open("input.txt") as f:
    input = f.read().splitlines()

input_int = [int(line or 0) for line in input]

cur_tot = 0
totals = []

for n in input_int:
    if n:
        cur_tot += n
    else:
        heapq.heappush(totals, cur_tot)
        cur_tot = 0

# No bonus points for efficiency, so use heapq for fewer lines :)
highest = heapq.nlargest(1, totals)
sum_top_3 = sum(heapq.nlargest(3, totals))

print(f"Part 1: {highest}")
print(f"Part 2: {sum_top_3}")