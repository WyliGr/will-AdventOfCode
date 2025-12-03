# Advent of Code - 2025 Edition
# Day03 - Part01

listToSum = []


def find_twelve_digit_number(digits_list):
    selected_digits = []
    left_pointer = 0
    for i in range(12):
        right_boundary = len(digits_list) - (11 - i)
        window = digits_list[left_pointer:right_boundary]
        max_value = max(window)
        max_idx_in_window = window.index(max_value)
        selected_digits.append(max_value)
        left_pointer = left_pointer + max_idx_in_window + 1
    return selected_digits


with open("input", "r") as file:
    for line in file:
        digits = [int(c) for c in line.strip()]
        selected_digits_list = find_twelve_digit_number(digits)
        number_str = "".join(str(n) for n in selected_digits_list)
        current_max = int(number_str)
        listToSum.append(current_max)

result = sum(listToSum)
print(result)
