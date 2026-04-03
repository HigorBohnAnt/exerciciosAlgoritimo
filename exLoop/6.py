num = int(input("Digite um numero para calcular o fatorial: "))
fatorial = 1
for i in range(1, num + 1):
    fatorial *= i
    print(fatorial)