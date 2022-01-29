hora:int

hora = int(input("Digite uma hora do dia:"))

if hora > 12 and hora > 18 :
    print("Boa tarde!")
elif hora > 18 :
    print("Boa noite!")
else :
    print("Bom dia!")


