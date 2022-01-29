i: int; j:int

n= int(input("Qual a ordem da matriz:"))

mat = [[0 for x in range (n) ]for x in range (n)]

for i in range (0,n):
    for j in range (0,n):
        mat[i][j]= int(input(f"ELEMENTO [{i},{j}]:"))

print("DIAGONAL PRINCIPAL:")
for i in range (0,n):
    print(f"{mat[i][i]}", end=" ")
print()
neg: int = 0
for i in range(0, n):
    for j in range (0, n):
        if mat[i][j] < 0 :
            neg= neg + 1
print(f"QUANTIDADES DE NEGATIVOS = {neg}")


