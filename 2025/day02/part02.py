# Advent of Code - 2025 Edition
# Day02 - Part 02

invalid_id = []

with open("input", "r") as file:
    content = file.read()

chars_bulk = []
ids = []

for char in content:
    if char.isdigit():
        chars_bulk.append(char)
    elif char in ",-":
        if chars_bulk:
            ids.append(int("".join(chars_bulk)))
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

    for number in range(first_id, second_id + 1):
        s = str(number)
        L = len(s)
        for k in range(1, L // 2 + 1):
            if L % k != 0:
                continue
            chunks = [s[i : i + k] for i in range(0, L, k)]
            if all(chunk == chunks[0] for chunk in chunks):
                invalid_id.append(number)
                break

result = sum(invalid_id)
print(result)
