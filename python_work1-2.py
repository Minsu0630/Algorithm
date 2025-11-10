grid = []
for _ in range(9):
    row_strings = input().split()
    row = [int(s) for s in row_strings]
    grid.append(row)

max_value = -1
max_row = 0
max_col = 0

for r in range(9):
    for c in range(9):
        if grid[r][c] > max_value:
            max_value = grid[r][c]
            max_row = r
            max_col = c

print(max_value)
print(f"{max_row + 1} {max_col + 1}")
