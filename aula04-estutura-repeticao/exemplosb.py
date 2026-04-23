nota1 = float(input("Digite a primeira nota: "))
while nota1 < 0 or nota1 > 10:
    print("A nota deve estar entre 0 e 10")
    nota1 = float(input("Digite a nota novamente: "))

nota2 = float(input("Digite a segunda nota: "))
while nota2 < 0 or nota2 > 10:
    print("A nota deve estar entre 0 e 10")
    nota2 = float(input("Digite a nota novamente"))

media = (nota1 + nota2) / 2

print(f"A media será de: {media}")


def receber_nota(a,b):
    return (a+b) / 2

print(f"A média é: {receber_nota(5,10)}")



