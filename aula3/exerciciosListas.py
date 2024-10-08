print("1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.")

vetor = []
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)

print(vetor)

print("\n2. Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.")

vetor2 = []
for i in range(10):
    numero = float(input(f"Digite o {i+1}º número: "))
    vetor2.append(numero)

vetor2.sort(reverse=True)
print(vetor2)

print("\n3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.")

nummedia1 = float(input("Digite a primeira nota: "))
nummedia2 = float(input("Digite a segunda nota: "))
nummedia3 = float(input("Digite a terceira nota: "))
nummedia4 = float(input("Digite a quarta nota: "))

print("Notas:")
print("1ª Nota: ", nummedia1)
print("2ª Nota: ", nummedia2)
print("3ª Nota: ", nummedia3)
print("4ª Nota: ", nummedia4)
print("\nMédia: ",(nummedia1 + nummedia2 + nummedia3 + nummedia4) / 4)

print("\n4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.")

vetor3 = []
for i in range(10):
    caractere = input(f"Digite o {i+1}º caractere: ")
    vetor3.append(caractere)

consoantes = 0

print("\n-----\n")

for caractere in vetor3:
    if caractere.lower() in 'bcdfghjklmnpqrstvwxyz':
        consoantes += 1
        print(f"Consoante encontrada: {caractere}")

# Mostra o resultado
print(f"\nQuantidade de consoantes: {consoantes}")

print("\n5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.")

numeros = []
PAR = []
IMPAR = []

for i in range(20):
    num = int(input("Digite um inteiro: "))
    numeros.append(num)

for num in numeros:
    if num % 2 == 0:
        PAR.append(num)
    else:
        IMPAR.append(num)

print("A lista original de números é:")
print(numeros)
print("A lista de números pares é:")
print(PAR)
print("A lista de números ímpares é:")
print(IMPAR)

print("\n6. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.")

alunos = []

for i in range(10):

    notas = []

    for j in range(4):
        nota = float(input(f"Digite a nota {j+1} do aluno {i+1}: "))
        notas.append(nota)

    alunos.append((i+1, (sum(notas) / len(notas))))

contagem = sum(1 for _, media in alunos if media >= 7.0)

print(f"Alunos com média maior ou igual a 7.0: {contagem}")
    
print("\n7. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.")

numeros = [int(input(f"Digite o número {i+1}: ")) for i in range(5)]

soma = sum(numeros)

multiplicacao = 1

for num in numeros:
    multiplicacao *= num

print(f"Soma: {soma}")
print(f"Multiplicação: {multiplicacao}")
print(f"Números: {numeros}")

print("\n8. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.")

idades = []
alturas  = []

for i in range(5):
    idade = int(input(f"Idade da pessoa {i+1}: "))
    altura = float(input(f"Altura da pessoa {i+1}: "))
    idades.append(idade)
    alturas.append(altura)

print("Idades em ordem inversa:")
idades.sort(reverse=True)
for idade in idades:
    print(idade)
    
print("Alturas em ordem inversa:")
alturas.sort(reverse=True)
for altura in alturas:
    print(altura)
    
print("\n9. Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.")

A = []

for i in range(10):
    numerossoma = int(input(f"Digite o {i+1}º número: "))
    A.append(numerossoma)
    
soma_quadrados = sum(A)
print("\nSoma dos números do vetor:",soma_quadrados)

print("\n10. Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.")

vetor4 = []
vetor5 = []

print("Digite os elementos do vetor 1:")
for i in range(10):
    elemento = int(input(f"Digite o {i+1}º elemento: "))
    vetor4.append(elemento)

print("\nDigite os elementos do vetor 2:")
for i in range(10):
    elemento = int(input(f"Digite o {i+1}º elemento: "))
    vetor5.append(elemento)

vetor_intercalado = []
for i in range(10):
    vetor_intercalado.append(vetor4[i])
    vetor_intercalado.append(vetor5[i])

print("\nVetor intercalado:")
for i, elemento in enumerate(vetor_intercalado):
    print(f"Elemento {i+1}: {elemento}")
    
print("\n11. Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.")

vetor6 = []
vetor7 = []
vetor8 = []

print("Digite os elementos do vetor 1:")
for i in range(10):
    elemento = int(input(f"Digite o {i+1}º elemento: "))
    vetor6.append(elemento)

print("\nDigite os elementos do vetor 2:")
for i in range(10):
    elemento = int(input(f"Digite o {i+1}º elemento: "))
    vetor7.append(elemento)
    
print("\nDigite os elementos do vetor 3:")
for i in range(10):
    elemento = int(input(f"Digite o {i+1}º elemento: "))
    vetor8.append(elemento)

vetor_intercalado = []
for i in range(10):
    vetor_intercalado.append(vetor6[i])
    vetor_intercalado.append(vetor7[i])
    vetor_intercalado.append(vetor8[i])

print("\nVetor intercalado:")
for i, elemento in enumerate(vetor_intercalado):
    print(f"Elemento {i+1}: {elemento}")
    
print("\n12. Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.")

idades1 = []
alturas1 = []

for i in range(30):
    idade = int(input(f"Informe a idade do aluno {i+1}: "))
    altura = float(input(f"Informe a altura do aluno {i+1}: "))
    idades1.append(idade)
    alturas1.append(altura)

media_altura = sum(alturas1) / len(alturas1)

contador1 = 0

for i in range(30):
    if idades1[i] > 13 and alturas[i] < media_altura:
        contador1 += 1

print(f"Existem {contador1} alunos com mais de 13 anos e altura inferior à média de {media_altura} metros.")