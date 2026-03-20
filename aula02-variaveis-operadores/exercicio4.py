distancia = 150
velocidadeMedia = 60

calculoDistancia = distancia / velocidadeMedia

arredondado = int(calculoDistancia)
minutos = (calculoDistancia - arredondado) * 60

print(f"O carro levou {arredondado} horas e {minutos} minutos")