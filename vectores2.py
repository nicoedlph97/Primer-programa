#VECTORES
#IMPRIMIR LOS DATOS IMPARES A 3

A = [1,5,8,9,30,9,13]
B = []

for i in A:
    if i > 3 and i % 2 != 0:
        B.append(i)

print(B)