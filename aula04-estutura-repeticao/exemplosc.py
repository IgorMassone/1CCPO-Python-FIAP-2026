# def receber_notas(mensagem):
#     while True:
#         try:
#             nota = float(input(mensagem))
#             if not (0<=nota<=10):
#                 print("Nota deve ser entre 0 e 10")
#                 continue
#             return nota
#         except ValueError:
#             print("Digite um número válido")

# def calcular_media(nota1,nota2):
#     media = (nota1 + nota2) / 2
#     return media

# nota1 = receber_notas("Digite o primeiro número: ")
# nota2 = receber_notas("Digite o segundo número: ")
# media = calcular_media(nota1,nota2)

# print(f"A média das notas {nota1:.2f} e {nota2:.2f} é de: {media:.2f}")
