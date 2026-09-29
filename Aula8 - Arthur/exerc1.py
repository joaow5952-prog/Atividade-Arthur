frase = input("Digite uma frase: ")

vogais = 0
espacos = 0
numeros = 0
especiais = 0

for caractere in frase:
    if caractere.lower() in "aeiouáéíóúâêôãõàü":
        vogais += 1
    elif caractere == " ":
        espacos += 1
    elif caractere.isdigit():
        numeros += 1
    elif not caractere.isalpha():
        especiais += 1

print()
print("Vogais:", vogais)
print("Espaços:", espacos)
print("Números:", numeros)
print("Caracteres especiais:", especiais)