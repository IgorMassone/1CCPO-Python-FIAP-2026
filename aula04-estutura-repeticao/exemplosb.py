def verificar_nota(nota):
    while nota < 0 or nota > 10:
        print("A nota deve estar entre 0 e 10")
        nota = float(input("Digite a nota novamente: "))
    return nota

#nota1 = verificar_nota(float(input("Digite a primeira nota: ")))
nota1 = float(input("Digite a primeira nota: "))
nota1 = verificar_nota(nota1)

nota2 = float(input("Digite a segunda nota: "))
nota2 = verificar_nota(nota2)
#nota2 = verificar_nota(float(input("Digite a segunda nota: ")))


media = (nota1 + nota2) / 2

print(f"A media será de: {media}")


def receber_nota(a,b):
    return (a+b) / 2

print(f"A média é: {receber_nota(5,10)}")



