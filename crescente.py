x:int;y:int
print(f"Digite dois numeros:")
x : int = (input())
y : int = (input())

while y != x:
    if x < y:
        print(f"CRESCENTE!")
    else:
        print(f"DECRESCENTE!")
    print(f"Digite outros dois numeros:")
    x = int(input())
    y = int(input())