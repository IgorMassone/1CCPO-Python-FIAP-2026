def verificar_numero(texto):
    texto = "".join(texto.split()).lower()

    return texto == texto[::-1]

print(verificar_numero("radar"))