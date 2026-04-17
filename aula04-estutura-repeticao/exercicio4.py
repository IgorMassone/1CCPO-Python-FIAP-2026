# soma = 0

# for i in range (1,6):
#     valor = float(input(f"Digite o {i}° valor"))
#     soma += valor
# print(soma)

valores = []

for i in range (1,6):
    valor = float(input(f"Digite o {i}° valor: "))
    valores.append(valor)

print(f"\n O maior valor é {max(valores)}")