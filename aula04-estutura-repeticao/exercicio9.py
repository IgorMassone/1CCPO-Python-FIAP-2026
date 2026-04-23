linhas = int(input("Digite a altura de linhas que deseja: "))

for i in range(1, linhas):
    espacos = ' ' * (linhas - i)
    asteriscos = '*' * i
    print(espacos, asteriscos)