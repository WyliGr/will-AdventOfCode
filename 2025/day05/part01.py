# Advent of Code - 2025 Edition
# Day05 - Part01

compteur_ligne = 0
all_ranges = []
count_in_range = 0
count_total_tested = 0

with open("input", "r") as file:
    for line in file:
        compteur_ligne += 1
        plage_str = line.strip()

        if not plage_str:
            continue

        if compteur_ligne <= 185:
            if "-" in plage_str:
                try:
                    min_borne, max_borne = map(int, plage_str.split("-"))
                    all_ranges.append((min_borne, max_borne))
                except ValueError:
                    pass
        else:
            try:
                nombre_a_tester = int(plage_str)
                count_total_tested += 1
                est_trouve = False

                for min_borne, max_borne in all_ranges:
                    if min_borne <= nombre_a_tester <= max_borne:
                        est_trouve = True
                        break

                if est_trouve:
                    count_in_range += 1

            except ValueError:
                pass

print(f"Nombre de nombres qui sont dans une des plages : {count_in_range}")
