desconto = 0
salario = int(input("Digite o salário: "))
if salario >= 5000:
    desconto = salario * 0.10
    print("Desconto foi de: R$:", desconto)
else:
    desconto = salario * 0.05
    print("Desconto foi de: R$:", desconto)