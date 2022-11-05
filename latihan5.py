print("Praktikum2")

A = int (input("Masukkan bilangan pertama:"))
B = int (input("Masukkan bilangan kedua: "))
C = int (input("Masukkan bilangan ketiga: "))

if A > B > C :
    print("\nBilangan pertama adalah bilangan terbesar = %s" % A)
elif B > C :
    print("\nBilangan kedua adalah bilangan terbesat = %s" % B)
else :
    print("\nBilangan ketiga adalah bilangan terbesar = %s" % C)