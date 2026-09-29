quantidade = int(input("Quantos alunos serão cadastrados? "))

alunos = []

for i in range(quantidade):
    print(f"\nAluno {i + 1}")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    curso = input("Curso: ")
    nota = float(input("Nota: "))

    aluno = {
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "nota": nota
    }
    alunos.append(aluno)

# Cálculos do relatório
soma_notas = 0
aprovados = []
maior = alunos[0]
menor = alunos[0]
maiores_de_idade = 0
por_curso = {}

for aluno in alunos:
    soma_notas += aluno["nota"]

    if aluno["nota"] >= 7:
        aprovados.append(aluno["nome"])

    if aluno["nota"] > maior["nota"]:
        maior = aluno

    if aluno["nota"] < menor["nota"]:
        menor = aluno

    if aluno["idade"] >= 18:
        maiores_de_idade += 1

    curso = aluno["curso"]
    if curso in por_curso:
        por_curso[curso] += 1
    else:
        por_curso[curso] = 1

media = soma_notas / len(alunos)

# Relatório
print("\n===== RELATÓRIO =====")
print(f"Média da turma: {media:.2f}")

print("Alunos aprovados:", ", ".join(aprovados) if aprovados else "Nenhum")

print(f"Aluno com maior nota: {maior['nome']} ({maior['nota']})")
print(f"Aluno com menor nota: {menor['nome']} ({menor['nota']})")

print("Quantidade de alunos maiores de idade:", maiores_de_idade)

print("Quantidade de alunos por curso:")
for curso, qtd in por_curso.items():
    print(f"  {curso}: {qtd}")