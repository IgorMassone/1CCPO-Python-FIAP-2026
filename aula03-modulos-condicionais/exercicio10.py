def receber_dados():
    salario = float(input("Insira o seu salário: "))
    return salario

def reajuste(salario):
    if salario <= 280:
        percentual = 20
    elif salario <= 700:
        percentual = 15
    elif salario <= 1500:
        percentual = 10
    else:
        percentual = 5

    aumento = salario * (percentual/100)
    return aumento, percentual

salario = receber_dados()
aumento, percentual = reajuste(salario)
total = salario + aumento

print(f"O salário atual antes do reaumento era de: R${salario:.2f} ")
print(f"O percentual de aumento foi de: {percentual}%")
print(f"O aumento será de R${aumento:.2f}")
print(f"O salário atual é de R${total:.2f}")