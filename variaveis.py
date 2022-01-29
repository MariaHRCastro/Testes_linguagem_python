salario1:float
salario2:float
nome1: str
nome2:str
idade:int
sexo:str

nome1 = input("NOME DA PRIMEIRA PESSOA:")
salario1 = float(input("SALARIO DA PRIMEIRA PESSOA:"))

nome2 = input("NOME DA SEGUNDA PESSOA:")
salario2 = int(input("SALARIO DA SEGUNDA PESSOA:"))

idade = int(input("DIGITE UMA IDADE:"))
sexo = input("DIGITE UM SEXO (F/M :")

print(f"Nome 1: {nome1}")
print(f"Salario 1:{salario1:.2f}")
print(f"Nome 2 : {nome2}")
print(f"Salario 2: {salario2}")
print(f"Idade: {idade}")
print(f"Sexo: {sexo}")