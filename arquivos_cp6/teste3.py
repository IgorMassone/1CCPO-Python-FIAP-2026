class Medidor:
    def __init__(self, local):
        self.local = local
        historico = []

    def registrar(self, kwh):
        if kwh < 0:
            print("Leitura Inválida")
        else:
            self.historico.append(kwh)

m = Medidor("Bloco A")
m.registrar(120)
print(m.historico)