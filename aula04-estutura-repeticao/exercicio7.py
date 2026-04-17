def ler_numero():
    while True:
        try:
            numero = int(input("Digite um número: "))
            return numero
        except ValueError:
            print("Digite um número válido!")

def lacofor(numero):
    for i in range(1, numero):
        if numero % i == 0:
            print(i)


numero = ler_numero()
lacofor(numero)