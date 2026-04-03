num = int(input("Digite um numero fibonate: "))
for i in range(1, num + 1):
    
    if i == 1 or i == 2:
        print(1)
    else:
        a, b = 1, 1
        for _ in range(3, i + 1):
            a, b = b, a + b
        print(b)
