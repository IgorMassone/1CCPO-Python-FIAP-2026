class Sensor:
    def __init__(self, codigo):
        self.codigo = codigo
        self.ativo = True
    
    def desligar(self):
        self.ativo = False

s1 = Sensor("S1")
s2 = Sensor("S2")

sensores = [s1, s2]
sensores[0].desligar()
