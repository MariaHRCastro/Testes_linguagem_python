print("DADOS DA PRIMEIRA PESSOA:")
nome1 = input("NOME 1:")
idade1= int(input("IDADE 1:"))
print("DADOS DA SEGUNDA PESSOA:")
nome2 = input("NOME 2:")
idade2= int(input("IDADE 2:"))

media:float = (idade1+idade2)/2
print(f"A idade media de {nome1} e {nome2} eh de {media:.1f} anos .")