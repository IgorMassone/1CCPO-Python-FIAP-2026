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
# print(aluno1.disciplinas[1].professor)

# adicionar notas do aluno referente às disciplinas
aluno1.adicionar_nota(sers, 10)
aluno1.adicionar_nota(sers, 8)
aluno1.adicionar_nota(cs, 5)
aluno1.adicionar_nota(cs, 3)

# print(aluno1.notas_por_disciplina)

print(aluno1.calcular_media_d(cs))
print(aluno1.calcular_media_g())