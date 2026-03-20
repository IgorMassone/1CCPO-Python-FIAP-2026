nomePeca = (input("Digite o nome da peça: "))
qntdPeca = int(input("Digite a quantidade de pecas: "))
valUnit = float(input("Digite o valor de cada peca: "))

nomePeca2 = (input("Digite o nome da segunda peça: "))
qntdPeca2 = int(input("Digite a quantidade de pecas: "))
valUnit2 = float(input("Digite o valor de cada peca: "))

calculoPeca = (valUnit * qntdPeca) + (valUnit2 + qntdPeca2)

print(f"Ao comprar as peças {nomePeca} e {nomePeca2}, você pagará {calculoPeca:.2f} reais ao todo")