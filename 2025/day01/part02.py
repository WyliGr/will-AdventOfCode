# Advent of Code - 2025 Edition
# Day01 - Part 02

value = 50
zero = 0

with open("input", "r") as file:
    line = file.readline()

    while line:
        direction = line[0].upper()
        step = int(line[1:])

        if direction == "L":
            for i in range(1, step + 1):
                value = (value - 1) % 100
                if value == 0:
                    zero += 1

        elif direction == "R":
            for i in range(1, step + 1):
                value = (value + 1) % 100
                if value == 0:
                    zero += 1

        line = file.readline()

print(zero)
