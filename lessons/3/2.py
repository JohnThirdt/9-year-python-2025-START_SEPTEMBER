print("F = A -> B")

print("G = NOT A OR B")

print("A B | F | G")
for x in [0, 1]:
    for y in [0, 1]:
        F = (x <= y)

        G = (not x or y)


        print(f"{x} {y} | {int(F)} | {int(G)}")