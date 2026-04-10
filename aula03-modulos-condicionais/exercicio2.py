def calcular(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"

def main():
    numero = int(input("Digite um numero: "))
    resposta = calcular(numero)
    print(resposta)

if __name__ == "__main__":
    main()