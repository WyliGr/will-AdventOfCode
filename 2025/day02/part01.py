# Advent of Code - 2025 Edition
# Day02 - Part 01

invalid_id = []

file = open("input", "r")
content = file.read()

chars_bulk = []
ids = []

for char in content:
    if char.isdigit():
        chars_bulk.append(char)
    elif char in ",-":
        if chars_bulk:
            char_joined = "".join(chars_bulk)
            ids.append(int(char_joined))
            chars_bulk.clear()
    elif char == "\n":
        continue
    else:
        print("Error occurred:", repr(char))

if chars_bulk:
    ids.append(int("".join(chars_bulk)))

for u in range(0, len(ids) - 1, 2):
    first_id = ids[u]
    second_id = ids[u + 1]
    for i in range(first_id, second_id + 1):
        if len(str(i)) % 2 == 0:
            mid = int(len(str(i)) / 2)
            text = str(i)
            i1 = text[:mid]
            i2 = text[mid:]
            if i1 == i2:
                invalid_id.append(i)
            elif i1[0] == 0:
                invalid_id.append(i)
            else:
                continue
        else:
            continue

result = sum(invalid_id)
print(result)
