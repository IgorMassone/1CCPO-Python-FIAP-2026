
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
        print(soma)#Mostra a cada interação no loop. 
    print(soma)#Mostra apenas o valor final


numero = whilenumero()
lacofor(numero)