nota1 = float(input("Digite a primeira nota: "))
while 0 <= nota1 <= 10:
    print("Nota 1 armazenada")
    break

nota2 = float(input("Digite a segunda nota: "))
while 0 <= nota2 <= 10:
    print("Nota 2 armazenada")
    break

media = (nota1 + nota2) / 2

print(f"A media será de: {media}")


def receber_nota(a,b):
    return (a+b) / 2

print(f"A média é: {receber_nota(5,10)}")



