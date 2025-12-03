# Advent of Code - 2025 Edition
# Day03 - Part01

listToSum = []

with open("input", "r") as file:
    for line in file:
        sliced = line.strip()
        current_max = 0

        for i in range(len(sliced) - 1):
            for j in range(i + 1, len(sliced)):
                tens = int(sliced[i])
                ones = int(sliced[j])
                number = (tens * 10) + ones

                if number > current_max:
                    current_max = number

        listToSum.append(current_max)

result = sum(listToSum)
print(result)
