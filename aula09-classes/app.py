from aluno import Aluno
from disciplina import Disciplina

# criar / instanciar 1 aluno
aluno1 = Aluno("Igor", "123456", "Ciência da Computação")

# criar / instanciar 2 disciplinas
sers = Disciplina("Soluções Renováveis", "Tritiack")
cs = Disciplina("Computer Science", "Lucas")

# print(cs.professor)
# sers.exibir_infos()

# matricular o aluno nas disciplinas
aluno1.matricular(sers)
aluno1.matricular(cs)
print(aluno1.disciplinas[1].professor)