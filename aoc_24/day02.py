"""
day 2
"""
from aocd import get_data
data = get_data(year=2024, day=2)

# part 1
input = data
inp = [list(map(int, line.split())) for line in input.splitlines()]
n = 0
for row in inp:
    diffs = [b - a for a, b in zip(row, row[1:])]
    if all(1 <= abs(d) <= 3 for d in diffs) and (all(d > 0 for d in diffs) or all(d < 0 for d in diffs)):
        n += 1
print(n)

# part 2
input = data
inp = [list(map(int, line.split())) for line in input.splitlines()]

def is_safe(row):
    diffs = [b - a for a, b in zip(row, row[1:])]
    return all(1 <= abs(d) <= 3 for d in diffs) and (all(d > 0 for d in diffs) or all(d < 0 for d in diffs))

n = 0
for row in inp:
    if is_safe(row):
        n += 1
    else:
        for i in range(len(row)):
            new_row = row[:i] + row[i+1:]
            if is_safe(new_row):
                n +=1
                break
print(n)