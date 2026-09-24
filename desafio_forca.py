import random

print("Bem-vindo ao programa de adivinhamentos da palavra")


palavras = {"frutas": ["banana", "morango", "pera", "abacaxi", "melancia"],
            "cores": ["azul", "vermelho", "verde", "amarelo", "preto"]
            }

def main():
    while True:
        print("\nEscolha uma categoria:")
        print("1 - Frutas")
        print("2 - Cores")
        print("3 - Sair")

        opcao = input("Digite o número da opção: ")

        if opcao == "1":
           categoria = "frutas"
        elif opcao == "2":
            categoria = "cores"
        elif opcao == "3":
            break
        else:
            print("Opção inválida! Tente novamente.")
            continue
        lista_palavras = palavras[categoria]
        total_palavras = len(lista_palavras)

        print(f"\nA categoria possui {total_palavras} palavras.")


        posicao = int(input(f"Escolha a posição da palavra (1 a {total_palavras}): "))

        if 1 <= posicao <= total_palavras:
            palavra_secreta = lista_palavras[posicao - 1]

        


if __name__ == "__main__":
    main()