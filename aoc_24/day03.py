"""
day 3
"""
from aocd import get_data
data = get_data(year=2024, day=3)

# part 1
import re
input = data
muls = re.findall(r'mul\((\d+),(\d+)\)', input)
multis = [int(a) * int(b) for a, b in muls]
multis_sum = sum(multis)

# part 2
muls = re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", input)
mul_ls = [] 
enabled = True 
for n in range(len(muls)): 
    m = muls[n] 
    if m =="don't()": 
        enabled = False 
    elif m == 'do()': 
        enabled = True 
    elif enabled and m.startswith('mul'): 
        mul_ls.append(re.findall(r'mul\((\d+),(\d+)\)', m)[0]) 
multis = [int(a) * int(b) for a, b in mul_ls]
multis_sum = sum(multis)
multis_sum