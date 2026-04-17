while True:
    try:
        numero = int(input("Digite um número: "))
        break
    except ValueError:
        print("Digite um número!")

soma = 0

for i in range(1, int(numero)):
    soma += i
    print(soma)

print(soma)