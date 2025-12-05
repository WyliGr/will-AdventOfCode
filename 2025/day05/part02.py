# Advent of Code - 2025 Edition
# Day05 - Part02

compteur_ligne = 0
all_ranges = []
total_fresh_ids = 0

with open("input", "r") as file:
    for line in file:
        compteur_ligne += 1
        if compteur_ligne > 185:
            break

        plage_str = line.strip()

        if not plage_str:
            continue

        if "-" in plage_str:
            try:
                min_borne, max_borne = map(int, plage_str.split("-"))
                all_ranges.append([min_borne, max_borne])
            except ValueError:
                pass

if not all_ranges:
    total_fresh_ids = 0
else:
    all_ranges.sort(key=lambda x: x[0])

    merged_ranges = []
    current_min, current_max = all_ranges[0]

    for next_min, next_max in all_ranges[1:]:
        if next_min <= current_max + 1:
            current_max = max(current_max, next_max)
        else:
            merged_ranges.append([current_min, current_max])
            current_min, current_max = next_min, next_max

    merged_ranges.append([current_min, current_max])

    for min_val, max_val in merged_ranges:
        total_fresh_ids += max_val - min_val + 1

print(f"Nombre total d'IDs frais : {total_fresh_ids}")
