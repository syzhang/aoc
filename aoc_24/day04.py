"""
day 4
"""
from aocd import get_data
data = get_data(year=2024, day=4)

# part 1
grid = data.split('\n')

directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)] 
n_rows = len(grid[:][0]) 
n_cols = len(grid[0][:])
totals = 0
for r in range(n_rows): 
    for c in range(n_cols): 
        tmp = grid[r][c] 
        if tmp == 'X': 
            for d in directions: 
                if 0 <= r+3*d[0] < n_rows and 0 <= c+3*d[1] < n_cols: # check bounds
                    tmp1 = grid[r+d[0]][c+d[1]] 
                    tmp2 = grid[r+2*d[0]][c+2*d[1]]
                    tmp3 = grid[r+3*d[0]][c+3*d[1]]
                    if tmp1 == 'M' and tmp2 == 'A' and tmp3 == 'S':
                        totals += 1
print(totals)

# part 2
directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)] 
n_rows = len(grid[:][0]) 
n_cols = len(grid[0][:])
totals = 0
for r in range(n_rows): 
    for c in range(n_cols): 
        tmp = grid[r][c] 
        if tmp == 'A': 
            if 0 < r < n_rows-1 and 0 < c < n_cols-1:
                ul = grid[r-1][c-1]
                ur = grid[r-1][c+1]
                ll = grid[r+1][c-1]
                lr = grid[r+1][c+1]
                diag1 = {ul, lr} # set checks
                diag2 = {ur, ll}
                if diag1 == {'M', 'S'} and diag2 == {'M', 'S'}:
                    totals += 1
print(totals)