piramide = int(input("Digite o tamanho da pirâmide: "))

for i in range(piramide,0,-1):
    espacos = ' ' * (piramide - i)
    asteriscos = '*' * (2 - i - 1)
    print(espacos + asteriscos)
