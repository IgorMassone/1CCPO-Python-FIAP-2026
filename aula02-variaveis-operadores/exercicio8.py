valorProduto = float(input("Digite o valor do produto: "))
valorPago = float(input("Digite o valor que foi pago: "))

calctroco =  valorPago - valorProduto

print(f"Você receberá de troco: {calctroco:.2f} reais")