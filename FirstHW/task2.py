# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
x = y = z = [0, 1]
for i in x:
    for j in y:
        for k in z:
            print(f'i-j-k [{i} {j} {k}]')
            print(not (x + y + z) == (not x) * (not y) * (not z))
