"""
day 1
"""
from aocd import get_data
data = get_data(year=2024, day=1)

# part 1
input = data
# Split into lines and extract sorted integer lists
inp = input.splitlines()
inp_ls0 = sorted([int(x.split()[0]) for x in inp])
inp_ls1 = sorted([int(x.split()[1]) for x in inp])

# Calculate differences and sum
dif = [abs(inp_ls0[i] - inp_ls1[i]) for i in range(len(inp_ls0))]
dif_sum = sum(dif)

print(dif_sum)

# part 2
input = data
# Split into lines and extract integer lists
inp = input.splitlines()
inp_ls0 = [int(x.split()[0]) for x in inp]
inp_ls1 = [int(x.split()[1]) for x in inp]

# Calculate similarity score
sim_score = [x * inp_ls1.count(x) for x in inp_ls0]
sim_sum = sum(sim_score)

print(sim_sum)