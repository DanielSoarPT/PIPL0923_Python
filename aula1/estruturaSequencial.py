print("1. Faça um Programa que mostre a mensagem \"Alo mundo\" na tela.")
print("\nAlo mundo\n")


print("2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].")
num = int(input("\nInsira um número: "))
print("\nO número informado foi", num)


print("\n3. Faça um Programa que peça dois números e imprima a soma.")
num1 = float(input("\nInsira o primeiro número: "))
num2 = float(input("\nInsira o segundo número: "))
print(num1, "+", num2, "=", num1 + num2)


print("\n4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.")
nota1 = float(input("\nInsira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))
nota4 = float(input("Insira a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print("A média das notas é:", media)


print("\n5. Faça um Programa que converta metros para centímetros.")
metros = float(input("\nInsira o valor em metros: "))
centimetros = metros * 100
print(metros, "metros é igual a", centimetros, "centímetros")

print("\n6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.")
raio = float(input("\nInsira o raio do círculo: "))
area = 3.14159 * (raio ** 2)
print("A área do círculo é:", area)

print("\n7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.")
area1 = float(input('\nLado do quadrado em m: '))
area2 = area1 * area1
print ("Dobro da area do quadrado: " ,area2 * 2)

print("\n8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.")
valor_hora = float(input("\nQuanto você ganha por hora? "))
horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? "))
salario_total = valor_hora * horas_trabalhadas
print("Seu salário total no mês é:", salario_total)

print("\n9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.")
fh = float(input("\nInsira a temperatura em graus Fahrenheit: "))
c = 5 * ((fh-32) / 9)
print(fh, "graus Fahrenheit é igual a", c, "graus Celsius.")

print("\n10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.")
c1 = float(input("\nInsira a temperatura em graus Celsius: "))
fh1 = (c1 * 1.8) + 32
print(c1, "graus Celsius é igual a", fh1, "graus Fahrenheit.")

print("\n11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: \na) o produto do dobro do primeiro com metade do segundo. \nb) a soma do triplo do primeiro com o terceiro. \nc) o terceiro elevado ao cubo.")

num1 = int(input("\nInsira o primeiro número inteiro: "))
num2 = int(input("Insira o segundo número inteiro: "))
num3 = float(input("Insira um número real: "))

numa = (2 * num1) * (num2 / 2)
numb = (3 * num1) + num3
numc = num3 ** 3

print("\na) O produto do dobro do primeiro com metade do segundo é:", numa)
print("b) A soma do triplo do primeiro com o terceiro é:", numb)
print("c) O terceiro elevado ao cubo é:", numc)

print("\n12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58")
altura = float(input("\nInsira a sua altura em metros: "))
peso = (72.7*altura) - 58
print("O seu peso ideal é:", peso, "kg.")

print("\n13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: \nPara homens: (72.7*h) - 58 \nPara mulheres: (62.1*h) - 44.7")
h = float(input("\nInsira a sua altura em metros: "))
altura_homens = (72.7*h) - 58
altura_mulheres = (62.1*h) - 44.7
print("\nO peso ideal para homens é:", altura_homens, "kg.")
print("O peso ideal para mulheres é:", altura_mulheres, "kg.")

print("\n14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.")

pesopeixe = float(input("\nPeso do peixe em kg: "))
if pesopeixe > 50:
	excedente = pesopeixe - 50
	multa = excedente * 4
else:
	excedente = 0
	multa = 0
print ("Peso:", pesopeixe, "Kg")
print ("Excesso:", excedente, "Kg")
print ("Multa:", multa, "R$")

print("\n15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:")
print("\na) salário bruto.")
print("b) quanto pagou ao INSS.")
print("c) quanto pagou ao sindicato.")
print("d) o salário líquido.")
print("e) calcule os descontos e o salário líquido, conforme a tabela abaixo:")
print("\n+ Salário Bruto : R$ \n- IR (11%) : R$ \n- INSS (8%) : R$ \n- Sindicato ( 5%) : R$ \n= Salário Liquido : R$")
print("\nObs.: Salário Bruto - Descontos = Salário Líquido.")

valorhoras = float(input("\nValor que ganha por hora: "))
horasmes = int(input("Horas por mês: "))

salario_bruto = valorhoras * horasmes
inss = 8/100 * salario_bruto
sindicato = 5/100 * salario_bruto
ir = 11/100 * salario_bruto

salario_liquido = salario_bruto - inss - sindicato - ir

print (" + Salário Bruto: R$", salario_bruto)
print (" - IR: R$", ir)
print (" - INSS: R$", inss)
print (" - Sindicato: R$", sindicato)
print (" = Salário Liquido: R$", salario_liquido)

print("\n16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.")

area = float(input("\nInsira o tamanho da área a ser pintada em metros quadrados: "))

litros_necessarios = area / 3
latas_necessarias = int(litros_necessarios / 18)
preco_total = latas_necessarias * 80

print("\nQuantidade de latas de tinta a serem compradas:", latas_necessarias)
print("Preço total:", preco_total, "R$")

print("\n17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.")
print("Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:")
print("\ncomprar apenas latas de 18 litros;")
print("comprar apenas galões de 3,6 litros;")
print("misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.")