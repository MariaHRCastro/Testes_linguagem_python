import math
base = float(input("Base do retangulo:"))
altura = float(input("Altura do retangulo:"))

area = base * altura
print(f"AREA = {area:.4f}")

perimetro = (2*(base+altura))
print(f"PERIMETRO = {perimetro:.4f}")

diagonal = math.sqrt((base*base) + (altura*altura))
print(f"DIAGONAL = {diagonal:.4f}")