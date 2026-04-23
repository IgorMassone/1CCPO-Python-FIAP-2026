def validar_valor(valor):
    while valor < 0:
        print("Digite um valor positivo: ")
        valor = int(input("Digite um novo valor:"))
    return valor

qtd = int(input("Digite a quantidade do produto: "))
qtd = validar_valor(qtd)

for i in range(1, qtd + 1):
    print(f"{i}° Produto")