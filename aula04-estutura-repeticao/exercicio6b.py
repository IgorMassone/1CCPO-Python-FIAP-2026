
def whilenumero():
    while True:
        try:
            numero = float(input("Digite um número: "))
            return numero
        except ValueError:
            print("Digite um número!")

def lacofor(numero):
    soma = 0
    for i in range(1, int(numero)):  
        soma += i 
        print(soma)  
    print(soma)


numero = whilenumero()
lacofor(numero)