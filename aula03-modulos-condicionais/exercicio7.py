def recebe_idade():
    idade = int(input("Digite a sua idade: "))
    return idade

def pode_votar(idade):
    if idade < 16:
        print("Ainda é muito jovem")
    elif 16 <= idade < 18:
        print("Votar é opcional")
    elif idade >= 18:
        print("Votar é obrigatório")
    else:
        return 0


def main():
    idade = recebe_idade()
    pode_votar(idade)


if __name__ == '__main__':
    main()