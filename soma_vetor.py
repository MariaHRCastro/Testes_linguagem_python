n : int; i:int
n= int(input("Quantos numeros voce vai digitar?"))

vet : [float] = [0 for x in range(n)]
soma:float = 0
cont:int = 0
for i in range(0,n):
    vet[i]= float(input("Digite um numero:"))
    soma = soma + vet[i]
    cont = cont + 1
print(f"VALORES :",end="")
for i in range(0,n):
    print(f"{vet[i]:.1f}",end=" ")
print()
media = soma / cont
print(f"SOMA = {soma:.2f}")
print(f"MEDIA = {media:.2f}")







