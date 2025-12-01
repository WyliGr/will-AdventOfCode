# Advent of Code - 2025 Edition
# Day01 - Part 01

value = 50
zero = 0

file = open("input", "r")
input_file = file.readline()

while input_file:
    direction = input_file[0].upper()
    step = int(input_file[1:])

    match direction:
        case "L":
            value = (value - step) % 100
        case "R":
            value = (value + step) % 100
    input_file = file.readline()
    if value == 0:
        zero += 1
    else:
        continue
print(zero)
