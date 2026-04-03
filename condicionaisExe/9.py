resultado = 0
calculadora = input("Digite a operação (+, -, *, /): ")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))  
if calculadora == "+":
    resultado = num1 + num2
    print("O resultado da soma é:", resultado)
elif calculadora == "-":
    resultado = num1 - num2
    print("O resultado da subtração é:", resultado)
elif calculadora == "*":
    resultado = num1 * num2
    print("O resultado da multiplicação é:", resultado) 
elif calculadora == "/":
    resultado = num1 / num2
    print("O resultado da divisão é:", resultado)
else:
    print("Operação inválida")