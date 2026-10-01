from disciplina import Disciplina

class Aluno:
    def __init__(self, nome, rm, curso):
        self.nome = nome
        self.rm = rm
        self.curso = curso
        self.disciplinas = [] # [Disciplina, Disciplina, ...]
        self.notas_por_disciplina = {} # {'Modelagem Linear" : [nota1, nota2 ...]}
    
    def matricular(self, disciplina: Disciplina): #Tipo: Disciplina é a classe.
        self.disciplinas.append(disciplina)
        self.notas_por_disciplina.setdefault(disciplina.nome, []) #Setar um padrão inicial

    def adicionar_nota(self, disciplina: Disciplina, nota: float): #Tipo de dados
        self.notas_por_disciplina[disciplina.nome].append(nota)