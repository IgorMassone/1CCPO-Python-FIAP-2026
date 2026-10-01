class Disciplina:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor
    
    def exibir_infos(self):
        print(f"Disciplina: {self.nome} | Professor: {self.professor}")

# # TEMPORÁRIO
# model_lin = Disciplina("Modelagem Linear", "Rodolfo")
# model_lin.exibir_infos()