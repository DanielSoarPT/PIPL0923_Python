print("1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.")

nota = input("\nIntroduza uma nota entre 0-10: ")
condicao = nota.isdigit()
while not (condicao and float(nota) >= 0 and float(nota) <= 10):
    print("Nota Inválida, insira um valor válido.")
    nota = input("Introduza uma nota entre 0-10: ")
else:
    print("Nota válida")
    
print("\n2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.")

username = input("\nIntroduza um nome de usuário: ")
password = input("Introduza uma senha: ")
while username == password:
    print("Senha igual ao nome de usuário, insira uma senha diferente.")
    username = input("\nIntroduza um nome de usuário: ")
    assword = input("Introduza uma senha: ")
else:
    print("Nome de usuário e senha válidos.")
    
print("\n3. Faça um programa que leia e valide as seguintes informações:")
print("a) Nome: maior que 3 caracteres;")
print("b) Idade: entre 0 e 150;")
print("c) Salário: maior que zero;")
print("d) Sexo: 'f' ou 'm';")
print("e) Estado Civil: 's', 'c', 'v', 'd';")

while True:
    nome = input("\nNome: ")
    if len(nome) > 3:
        break
    print("Nome inválido. Deve ter mais de 3 caracteres.")

while True:
    idade = input("Idade: ")
    if idade.isdigit() and 0 <= int(idade) <= 150:
        break
    print("Idade inválida. Deve ser um número entre 0 e 150.")

while True:
    salario = input("Salário: ")
    try:
        if float(salario) > 0:
            break
    except ValueError:
        pass
    print("Salário inválido. Deve ser um número maior que zero.")

while True:
    sexo = input("Sexo (f/m): ").lower()
    if sexo in ['f', 'm', 'F', 'M']:
        break
    print("Sexo inválido. Deve ser 'f' ou 'm'.")

while True:
    estado_civil = input("Estado Civil (s/c/v/d): ").lower()
    if estado_civil in ['s', 'c', 'v', 'd', 'S', 'C', 'V', 'D']:
        break
    print("Estado Civil inválido. Deve ser 's', 'c', 'v' ou 'd'.")

print("\nInformações válidas:")
print("Nome:",nome)
print("Idade:",idade)
print("Salário:",salario)
print("Sexo:",sexo)
print("Estado Civil:",estado_civil)

print("\n4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.")

populacao_a = 80000
taxa_crescimento_a = 0.03
populacao_b = 200000
taxa_crescimento_b = 0.015
anos = 0

while populacao_a < populacao_b:
    populacao_a += populacao_a * taxa_crescimento_a
    populacao_b += populacao_b * taxa_crescimento_b
    anos += 1

# Exibição dos resultados
print("\nSerão necessários", anos, "anos para que a população do país A ultrapasse ou iguale a população do país B.")
print("População final do país A:", populacao_a)
print("População final do país B:", populacao_b)

print("\n5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.")

def obter_numero_positivo(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor
            else:
                print("Por favor, insira um número positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def obter_taxa_crescimento(mensagem):
    while True:
        try:
            taxa = float(input(mensagem))
            if 0 < taxa <= 100:
                return taxa / 100
            else:
                print("Por favor, insira uma taxa entre 0 e 100.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

while True:
    print("\nInforme os dados para o cálculo:")
    populacao_a = obter_numero_positivo("População inicial do país A: ")
    taxa_crescimento_a = obter_taxa_crescimento("Taxa de crescimento do país A (em %): ")
    populacao_b = obter_numero_positivo("População inicial do país B: ")
    taxa_crescimento_b = obter_taxa_crescimento("Taxa de crescimento do país B (em %): ")

    anos = 0

    while populacao_a < populacao_b:
        populacao_a += populacao_a * taxa_crescimento_a
        populacao_b += populacao_b * taxa_crescimento_b
        anos += 1

    print(f"\nSerão necessários", anos, "anos para que a população do país A ultrapasse ou iguale a população do país B.")
    print(f"População final do país A:", populacao_a)
    print(f"População final do país B:", populacao_b)
    break

print("Programa encerrado.")

print("\n6. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.")

num = 0
while num <= 20:
    print(num)
    num += 1

num = 0
while num <= 20:
    print(num, end=" ")
    num += 1
    
print("\n7. Faça um programa que leia 5 números e informe o maior número.")

numeros = []
for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

maior_numero = max(numeros)

print("O maior número é:", maior_numero)

print("\n8. Faça um programa que leia 5 números e informe a soma e a média dos números.")

num1 = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))
num3 = float(input("Digite o 3º número: "))
num4 = float(input("Digite o 4º número: "))
num5 = float(input("Digite o 5º número: "))

somanum = num1 + num2 + num3 + num4 + num5
media = somanum / 5

print("Soma dos números:", somanum)
print("Média dos números:", media)

print("\n9. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.")

for numero in range(1, 50):
    if numero % 2 != 0:
        print(numero)
        
print("\n10. Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.")

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

if num1 < num2:
   for numero in range(num1 + 1, num2):
       print(numero)
else:
   for numero in range(num2 + 1, num1):
       print(numero)
       
print("\n11. Altere o programa anterior para mostrar no final a soma dos números.")

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

if num1 < num2:
   for numero in range(num1 + 1, num2):
       print(numero)
else:
   for numero in range(num2 + 1, num1):
       print(numero)
       
soma = num1 + num2

print("Soma dos números:", soma)

print("\n12. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:")
print("Tabuada de 5:")
print("5 X 1 = 5")
print("5 X 2 = 10")
print("...")
print("5 X 10 = 50")

numero = int(input("Informe um número entre 1 e 10: "))

if 1 <= numero <= 10:
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
else:
    print("Número inválido. Por favor, informe um número entre 1 e 10.")