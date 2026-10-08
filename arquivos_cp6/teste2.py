class Turma:
    def __init__(self, codigo):
        self.codigo = codigo
        self.alunos = []
        self.notas = []
    
    def matricular(self, rm, nome, cps):
        self.alunos.append((rm, nome))
        self.notas.append(cps)
    
    def media(self, i):
        menor = self.notas[i][0]
        for nota in self.notas[i]:
            if nota < menor:
                menor = nota
        return (sum(self.notas[i]) - menor) / (len(self.notas[i]) - 1)
    
    def situacao(self):
        resumo = {"APROVADO": [], "EXAME": [], "REPROVADO": []}

        for i in range(len(self.alunos)):
            m = self.media(i)

            if m >= 6:
                chave = "APROVADO"
            elif m >= 4:
                chave = "EXAME"
            else:
                chave = "REPROVADO"
            
            resumo[chave].append(self.alunos[i][1])
        
        return resumo

t = Turma("1CCPK")
cps_caio = [2, 6, 2]

t.matricular(rm=101, nome="Ana", cps=[5, 6, 9])
t.matricular(rm=102, nome="Bia", cps=[3, 4, 5])
t.matricular(rm=103, nome="Caio", cps=cps_caio)
t.matricular(rm=104, nome="Duda", cps=[10, 1, 2])

cps_caio[0] = 7

r = t.situacao()
print(r["APROVADO"], len(r["EXAME"]), r["REPROVADO"])
    