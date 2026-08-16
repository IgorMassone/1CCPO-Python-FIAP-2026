temperaturas = [[28, 31, 34, 33],
                [25, 27, 29, 28],
                [32, 35, 36, 34],
                [24, 26, 25, 27]]
sala_maior_risco = -1
sala_registro = 0
critico = 0
for sala in temperaturas:
    sala_registro +=1
    contador = 0
    media = sum(sala) / len(sala)
    for temperatura in sala:
        if temperatura >= 33:
            contador += 1
    print(f"Sala {sala_registro}")
    print(f"Média: {media}")
    print(f"Registros críticos: {contador}\n")

    if contador >= critico:
        critico = contador
        sala_maior_risco = sala_registro

print(f"A sala com o maior risco: Sala {sala_maior_risco}")