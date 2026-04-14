codigo = int(input("Digite o código da carga: "))
peso_ton = float(input("Digite o peso da carga: "))
codigo_origem = int(input("Digite o código de origem da carga:  "))

peso_kg = peso_ton * 1000

if 10 <= codigo <= 20:
    carga = peso_kg * 100
elif 21 <= codigo <= 30:
    carga = peso_kg * 250
elif 31 <= codigo <= 40:
    carga = peso_kg * 340

if codigo_origem == 1:
    imposto = carga * 0.35
elif codigo_origem == 2:
    imposto = carga * 0.25
elif codigo_origem == 3:
    imposto = carga * 0.15
elif codigo_origem == 4:
    imposto = carga * 0.05
else:
    imposto = 0

total = carga + imposto

print(f"Peso em kg: {peso_kg:.2f} kg")
print(f"Preço da carga: R$ {carga:.2f}")
print(f"Imposto: R$ {imposto:.2f}")
print(f"Total: R$ {total:.2f}")