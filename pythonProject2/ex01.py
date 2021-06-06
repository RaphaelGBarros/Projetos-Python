x = 1
contanum=0
while x <= 10:
    numero = int(input("Digite um valor"))

    if numero >5:
        contanum=contanum+1

    x=x+1

print("numeros maires que cinco", contanum)