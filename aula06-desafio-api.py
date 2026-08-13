endpoints = ["/login", "/produtos", "/pedidos"]
status = [
[200, 200, 401, 200, 500],
[200, 200, 200, 200, 200],
[201, 500, 502, 201, 500]
]

# print(endpoints[0])
# print(status[0])

# FUNÇÃO QUE VERIFICA SE UM CÓDIGO HTTP DA REQ. DE UM 
# ENDPOINT É SUCESSO OU NÃO
# 200 --> True
# 4001 --> False

def eh_sucesso(codigo):
    return codigo >= 200 and codigo <= 299
# print(eh_sucesso(401))

# FUNÇÃO QUE VERIFICA SE TEM 2 ERROS SEGUIDOS
# NA LISTA DE REQUISIÇÕES DE 1 ENDPOINT
#[200, 200, 401, 200, 500] --> false
# [201, 500, 502, 201, 500] --> true

def dois_erros_seg(lista_req):
    for i in range(len(lista_req) - 1):
        codigo_atual = lista_req[i]
        prox_codigo = lista_req[i+1]

        if not eh_sucesso(codigo_atual) and not eh_sucesso(prox_codigo):
            return True
    return False

# print(dois_erros_seg(status[0]))


# NA LISTA DE REQUISIÇÕES DE 1 ENDPOINT
#[200, 200, 401, 200, 500] --> false
# [201, 500, 502, 201, 500] --> true
def analisa_endpoint(lista_req):
    qtd_sucessos = 0

    for codigo in lista_req:
        if eh_sucesso(codigo):
            qtd_sucessos += 1

    qtd_total_req = len(lista_req)
    qtd_erros = qtd_total_req - qtd_sucessos
    percentual_sucessos = (qtd_sucessos/qtd_total_req) * 100

    tem_erro_seguidos = dois_erros_seg(lista_req)

    if tem_erro_seguidos:
        classificacao = "CRÍTICO"
    elif percentual_sucessos >= 80:
        classificacao = "ESTÁVEL"
    else:
        classificacao = "INSTÁVEL"

    return (qtd_sucessos, qtd_erros, percentual_sucessos, classificacao)

# PERCORRER A MATRIZ status
qtd_maior_erro = -1
endpoint_maior_erro = ""
for i in range(len(endpoints)):
    nome_endpoint = endpoints[i]
    reqs_endpoint = status[i]

    sucessos, erros, percentual, classificacao = analisa_endpoint(reqs_endpoint)

    print(f"Endpoint: {nome_endpoint}")
    print(f"Requsições: {reqs_endpoint}")
    print(f"Sucessos: {sucessos}")
    print(f"Erros: {erros}")
    print(f"% de sucesso: {percentual}")
    print(f"Classificacao: {classificacao}")
    print("-"*30)
    print()

    if erros > qtd_maior_erro:
        qtd_maior_erro = erros
        endpoint_maior_erro = nome_endpoint

print(f"Endpoint maior erro: {endpoint_maior_erro} ({qtd_maior_erro})")