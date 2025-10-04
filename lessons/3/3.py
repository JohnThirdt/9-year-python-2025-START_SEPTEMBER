print("Закон Де-Моргана")

print("NOT ( X OR Y )  = NOT (X) AND NOT (Y)  ")

print("NOT ( X AND Y )  = NOT (X) OR NOT (Y)  ")

print("X Y | F | G")

for x in [0, 1]:
    for y in [0, 1]:
        F = not (x and y)
        G = not x or not y

        print(f"{x} {y} | {int(F)} | {int(G)} ")
