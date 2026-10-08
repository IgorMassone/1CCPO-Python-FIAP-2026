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

    def calcular_media_d(self, d: Disciplina) -> float:
        notas = self.notas_por_disciplina.get(d.nome, [])
        if not notas:
            return 0
        return sum(notas) / len(notas)
    
    def calcular_media_g(self) -> float:
        medias = []
        if not self.disciplinas:
            return 0
        for d in self.disciplinas:
            media_d = self.calcular_media_d(d)
            medias.append(media_d)
        
        return sum(medias) / len(medias)

    def exibir_boletim(self):
        print("=" * 50)
        print(f"BOLETIM - {self.nome} (RM {self.rm})")
        print(f"Curso: {self.curso}")
        print("=" * 50)

        for d in self.disciplinas:
            notas = self.notas_por_disciplina[d.nome]
            media = self.calcular_media_d(d)

            print(f"Disciplina: {d.nome}")
            print(f"Professor: {d.professor}")
            print(f"Notas: {notas}") # {', '.join(str(n) for n in notas)}
            print(f"Média: {media:.2f}")
            print("-" * 50)
