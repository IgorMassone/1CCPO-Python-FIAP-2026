def receber_dados():
    valorFornecido = int(input("Digite o valor: "))
    return valorFornecido

def loop(valorFornecido):
    for i in range(2, valorFornecido):
        if i % 2 == 0:
            print(f"{i}")

valorFornecido = receber_dados()

loop(valorFornecido)
