# Advent of Code - 2025 Edition
# Day04 - Part02

with open("input", "r") as file:
    grid = [list(line.strip()) for line in file]

rows = len(grid)
columns = len(grid[0])
directions = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]

total_removed = 0
removed_in_last_round = 1

while removed_in_last_round > 0:
    removed_in_last_round = 0
    rolls_to_remove = []

    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == "@":
                neighbor_count = 0
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < rows and 0 <= nc < columns:
                        if grid[nr][nc] == "@":
                            neighbor_count += 1

                if neighbor_count < 4:
                    rolls_to_remove.append((r, c))

    removed_in_last_round = len(rolls_to_remove)

    if removed_in_last_round > 0:
        for r_remove, c_remove in rolls_to_remove:
            grid[r_remove][c_remove] = "x"

        total_removed += removed_in_last_round

for row_list in grid:
    print("".join(row_list))

print(total_removed)
