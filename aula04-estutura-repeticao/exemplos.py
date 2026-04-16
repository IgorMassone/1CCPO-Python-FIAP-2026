def recebernumero():
    try:
        return int(input("Digite um número: "))
    except ValueError:
        print("Digite um número válido!")
        return recebernumero()


def contar(numero):
    contador = 0

    while contador < numero:
        print(contador)
        contador += 1

numero = recebernumero()

contar(numero)