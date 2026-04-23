# i = 4
#
# while i >= 1:
#     print(i)
#     i -= 1
#
# jogar = "SIM"
# while jogar.lower() == "sim":
#     print("Repete ou inicia o jogo")
#     jogar = input("Deseja jogar novamente?")

i = 0
while i < 10:
    i += 1

    if i == 3:
        continue

    if i == 7:
        break
    print(f"Produto: {i}")