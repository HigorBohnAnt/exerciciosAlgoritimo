imc = 0
peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))
imc = peso / (altura * altura)
if imc < 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("Peso normal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
else:
    print("obesidade")