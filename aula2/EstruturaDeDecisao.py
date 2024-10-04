print("\n1. Faça um Programa que peça dois números e imprima o maior deles.")

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    print("O maior número é:", n1)
else:
    print("O maior número é:", n2)

print("\n2.Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.")

val = int(input("Insira um valor: "))

if val > 0:
    print("O valor inserido é positivo: ")
else:
    print("O valor inserido é negativo: ")
    
print("\n3. Faça um Programa que verifique se uma letra digitada é 'F'' ou 'M'. Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.")

letra = input("Digite uma letra (M/F): ")

if letra.lower() == 'm':
    print("Masculino")
elif letra.lower() == 'f':
    print('Feminino')
else:
    print('Género inválido')
    
print("\n4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.")

letra = input("Digite uma letra: ")

vogais = ["a", "e", "i", "o", "u"]

if letra.lower() in vogais:
    print("É uma vogal")
else:
    print("É consoante")
    
print("\n5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:")
print("\nA mensagem 'Aprovado', se a média alcançada for maior ou igual a sete;")
print("A mensagem 'Reprovado', se a média for menor do que sete;")
print("A mensagem 'Aprovado com Distinção', se a média for igual a dez.")

nota1 = int(input("Digite a primeira nota (0-10): "))
nota2 = int(input("Digite a segunda nota (0-10): "))

media = (nota1 + nota2) / 2

if media > 7 and media < 10:
    print("Aprovado")
elif media == 10:
    print("Aprovado com Distinção")
else:
    print("Reprovado")

print("\n6. Faça um Programa que leia três números e mostre o maior deles.")

n1 = int(input("Digite um número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 > n2 and n1 > n3:
    print("O maior número é:", n1)
elif n2 > n1 and n2 > n3:
    print("O maior número é:", n2)
else:
    print("O maior número é:", n3)

print("\n7. Faça um Programa que leia três números e mostre o maior e o menor deles.")

n1 = int(input("Digite um número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 > n2 and n1 > n3:
    print("O maior número é:", n1)
elif n2 > n1 and n2 > n3:
    print("O maior número é:", n2)
else:
    print("O maior número é:", n3)

if n1 < n2 and n1 < n3:
    print("O menor número é:", n1)
elif n2 < n1 and n2 < n3:
    print("O menor número é:", n2)
else:
    print("O menor número é:", n3)

print("\n8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.")

preco1 = float(input("Preço produto nº1: "))
preco2 = float(input("Preço produto nº2: "))
preco3 = float(input("Preço produto nº3: "))

if preco1 < preco2 and preco1 < preco3:
    print("O produto que você deverá comprar custa:", preco1, "Euros")
elif preco2 < preco1 and preco2 < preco3:
    print("O produto que você deverá comprar custa:", preco2, "Euros")
else:
    print("O produto que você deverá comprar custa:", preco3, "Euros")

print("\n9. Faça um Programa que leia três números e mostre-os em ordem decrescente.")

n1 = int(input("Digite um número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 < n2 and n1 < n3:
    print(f"{n2}; {n1}; {n3}")
elif n2 < n1 and n2 < n3:
    print(f"{n1}; {n3}; {n2}")
else:
    print(f"{n3}; {n2}; {n1}")

print("\n10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem 'Bom Dia!', 'Boa Tarde!' ou 'Boa Noite!' ou 'Valor Inválido!', conforme o caso.")

turnoEscolhido = input("Escolha uma das 3 opções de turno: M: Matutino, V: Vespertino, N: Noturno").upper()

if turnoEscolhido == "M":
    print("Bom Dia!")
elif turnoEscolhido == "V":
    print("Boa Tarde!")
elif turnoEscolhido == "N":
    print("Boa Noite!")
else:
    print("Opção inválida")