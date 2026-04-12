def verificar_situacao(media):
    if media >= 7:
        print("Aprovado")
    elif media >= 5:
        print("Em recuperação")
    else:
        print("Reprovado")

def pedir_notas():
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    n4 = float(input("Digite a quarta nota: "))
    return (n1+n2+n3+n4)/4

def main():
    media = pedir_notas()
    verificar_situacao(media)

if __name__ == "__main__":
    main()