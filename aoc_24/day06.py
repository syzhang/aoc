"""
day 6
"""
from aocd import get_data
data = get_data(year=2024, day=6)

# part 1
input = data
grid = [list(row) for row in input.split('\n')]
for r in range(len(grid)): 
    for c in range(len(grid[r])): 
        if grid[r][c] == '^': 
            start = (r, c)

# First, find all positions the guard visits (from part 1)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir_idx = 0
r, c = start
visited_positions = {start}
while 0 <= r < len(grid) and 0 <= c < len(grid[0]): 
    dr, dc = directions[dir_idx] 
    next_r, next_c = r + dr, c + dc
    if 0 <= next_r < len(grid) and 0 <= next_c < len(grid[0]):
        if grid[next_r][next_c] == '#': 
            dir_idx = (dir_idx + 1) % 4 
        else: 
            r, c = next_r, next_c 
            visited_positions.add((r, c))
    else:
        break

# part 2
# Now test obstacles only at visited positions (excluding start)
os = 0
for gr, gc in visited_positions:
    if (gr, gc) == start:
        continue
    
    grid[gr][gc] = '#'
    
    # Run simulation
    r, c = start
    dir_idx = 0
    been = {(start, dir_idx)}
    
    while 0 <= r < len(grid) and 0 <= c < len(grid[0]): 
        dr, dc = directions[dir_idx] 
        next_r, next_c = r + dr, c + dc
        if 0 <= next_r < len(grid) and 0 <= next_c < len(grid[0]):
            if grid[next_r][next_c] == '#': 
                dir_idx = (dir_idx + 1) % 4 
            else: 
                r, c = next_r, next_c 
            
            if ((r, c), dir_idx) in been:
                os += 1
                break
            been.add(((r, c), dir_idx))
        else:
            break
    
    grid[gr][gc] = '.'

print(os)