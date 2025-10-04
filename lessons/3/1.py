print("F = (A and B) or not(B)")


print("A B | F")
for x in [0, 1]:
    for y in [0, 1]:
        F = (x and y) or not(y)


        print(f"{x} {y} | {int(F)}")