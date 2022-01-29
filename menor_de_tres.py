menor: int
a = int(input("Qual o primeiro valor?"))
b = int(input("Qual o segundo valor?"))
c = int(input("Qual o terceiro valor?"))

menor = a
if b < a and b < c :
    menor = b
elif c < a:
    menor = c

print(f"MENOR = {menor}")