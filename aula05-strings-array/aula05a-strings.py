texto = "Fiap Paulista"

print(texto[0])
print(texto[1])
print(texto[2])
print(texto[3])

tamanho_texto = len(texto)
print(tamanho_texto)

#For indexado
for i in range(tamanho_texto):
    print(f"Posição: {i}, {texto[i]}")

#For Each
for c in texto:
    print(c)