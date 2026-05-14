temperaturas = [[28, 31, 34, 33],
                [25, 27, 29, 28],
                [32, 35, 36, 34],
                [24, 26, 25, 27]]
sala_maior_risco = -1
critico = 0
# Calcula a média
for i in range(len(temperaturas)):
    contador = 0
    for j in range(len(temperaturas)):
        media = sum(temperaturas[i])/ len(temperaturas[j])
        if temperaturas[i][j] >= 33:
            contador += 1
    if contador > critico:
        critico = contador
        sala_maior_risco = i + 1
    print(f"Sala {1 + i}\n Média {media}\n Registros críticos {contador}\n")

print(f"Sala com maior risco: Sala {sala_maior_risco}")


