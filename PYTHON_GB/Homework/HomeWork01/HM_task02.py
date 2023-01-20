# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x_y_z = [
    [0,0,0],
    [0,0,1],
    [0,1,0],
    [1,0,0],
    [1,1,1],
    [1,1,0],
    [1,0,1],
    [0,1,1]
]
for i in range(8):
    a = not (x_y_z[i][0] or x_y_z[i][1] or x_y_z[i][2])
    b = not ((x_y_z[i][0] and not x_y_z[i][1] and not x_y_z[i][2]))
    if a != b:
        print("Выражение: ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - Ложь")
        break
else:
    print("Выражение: ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - Истина")

for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            if(not x or y or z) != (not x or y or z):
                print("Выражение: ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - Ложь")
                break
else:
    print("Выражение: ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - Истина")