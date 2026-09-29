quantidade = int(input("Quantas notas serão informadas? "))

notas = []

for i in range(quantidade):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)
maior = max(notas)
menor = min(notas)

aprovados = 0
for nota in notas:
    if nota >= 7:
        aprovados += 1

print()
print("Notas:", notas)
print(f"Média: {media:.2f}")
print("Maior nota:", maior)
print("Menor nota:", menor)
print("Aprovados:", aprovados)