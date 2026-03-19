print("Olá mundo")

print(7+4)
print("7 + 4")
print("7" + "4") # Concatenação de strings

# Comentários de 1 linha
'''
    Comentários de
    múltiplas
    linhas
    Autor: Igor Massone
    Versão: 1.0.1
'''

# Variáveis
nome = "Igor" #str
idade = 17 #int
peso = 58.2 #float

print(nome, idade, peso)
print(f"Oiiiii, {nome}!!!")

# INPUT - SIMULAÇÃO DE FORMULÁRIOS NO CMD

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idaede: "))
peso = float(input("Digite o seu peso: "))

print(nome, idade, peso)
print(idade + 1)

ano_nascimento = 2008
ano_atual = 2026
idade = ano_atual - ano_nascimento
print(f"A sua idade é: {idade}")