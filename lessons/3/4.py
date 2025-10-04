print("F = (A and B)  OR  (C and NOT(A))")

print("A B C | F")

for A in [0, 1]:
    for B in [0, 1]:
        for C in [0, 1]:
            F = (A and B) or (C and not A)
            print(f"{A} {B} {C} | {int(F)}")