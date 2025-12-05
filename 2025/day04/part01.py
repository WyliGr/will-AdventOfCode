# Advent of Code - 2025 Edition
# Day04 - Part01

with open("input", "r") as file:
    grid = [line.strip() for line in file]

rows = len(grid)
columns = len(grid[0])

print(rows)
print(columns)

directions = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]

accessibleRolls = 0

for row in range(rows):
    for col in range(columns):
        if grid[row][col] == "@":
            counted = 0
            for dr, dc in directions:
                r_neighbor = row + dr
                c_neighbor = col + dc

                if 0 <= r_neighbor < rows and 0 <= c_neighbor < columns:
                    if grid[r_neighbor][c_neighbor] == "@":
                        counted += 1

            if counted < 4:
                accessibleRolls += 1

print(accessibleRolls)
