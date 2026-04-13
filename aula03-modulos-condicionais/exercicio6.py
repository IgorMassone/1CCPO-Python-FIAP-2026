def ler_numeros():
    n1 = int(input("Digite o primeiro numero: "))
    n2 = int(input("Digite o segundo numero: "))
    operador = input("Digite o operador (+, -, *, /): ")
    return n1,n2, operador

def calculo(n1,n2,operador):
    if operador == "+":
        return (n1+n2)
    elif operador == "-":
        return (n1-n2)
    elif operador == "*":
        return (n1*n2)
    elif operador == "/":
        if n2 == 0:
            return "Erro: divisão por zero"
        else:
            return n1 / n2
    
def main():
    n1, n2, operador = ler_numeros()
    resultado = calculo(n1, n2, operador)
    print(f"O resultado é: {resultado}")


if __name__ == '__main__':
    main()