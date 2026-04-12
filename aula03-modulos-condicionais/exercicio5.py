def ler_valores():
    n1 = int(input("Digite o primeiro valor: "))
    n2 = int(input("Digite o segundo valor: "))
    return n1, n2

def calculo(n1,n2):
    if n1 % n2 == 0:
        print("São múltiplos")
    elif n2 % n1 == 0:
        print("São múltiplos")
    else:
        print("Não são múltiplos")

def main():
    n1, n2 = ler_valores()
    calculo(n1,n2)

if __name__ == "__main__":
    main()
