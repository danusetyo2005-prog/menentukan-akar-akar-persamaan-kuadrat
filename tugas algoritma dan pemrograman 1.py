import math

print("PROGRAM MENENTUKAN AKAR PERSAMAAN KUADRAT")

a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = float(input("Masukkan nilai c: "))

if a == 0:
    print("Bukan persamaan kuadrat.")
else:
    D = b**2 - 4*a*c

    print("Diskriminan =", D)

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)

        print("Persamaan memiliki dua akar real berbeda.")
        print("x1 =", x1)
        print("x2 =", x2)

    elif D == 0:
        x = -b / (2*a)

        print("Persamaan memiliki satu akar real kembar.")
        print("x =", x)

    else:
        print("Persamaan tidak memiliki akar real.")