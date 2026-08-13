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
print(eh_sucesso(401))