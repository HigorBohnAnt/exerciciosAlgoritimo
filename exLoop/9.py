soma = 0
cont = 0
med = 0
while True:
    num = int(input("Digite um numero: "))
    if num < 0:
        break 
    soma += num
    cont += 1

    med = soma / cont
    print("Sua media é:",med)

    