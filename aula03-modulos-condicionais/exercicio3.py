def logica_numero(num1,num2):
    if num1 > num2:
        print(f"O {num1} é maior que {num2}")
    elif num1 < num2:
        print(f"O {num1} é menor que {num2}")
    else:
        print("Os dois números são iguais")

def pedir_numero():
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    return num1, num2

def main():
    num1, num2 = pedir_numero()
    logica_numero(num1, num2)

if __name__ == "__main__":
    main()