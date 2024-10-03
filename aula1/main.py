#cmt

"""
cmt
varias
linhas

"""

#prt
print("Ola Mundo")


#var
nome = "Valor" # String
idade = 10 # max int em c -> 2,147,483,647, max int em Py -> não
nota = 10.9 # Float ( 6 a 7 ) e Double (14 )
aprovado = True


print(nome)
nome = 10
print(nome)



soma = idade + 3
print(soma)


soma2 = nota +2
print(soma2)


nome = "Valor"
soma3 = nome + " Foo"
print(soma3)


nome = "Valor"
# soma4 = nome + 2024
# print(soma4)

op5 = nome * 2
print(op5)

#print v2


nome = "Gonçalo"
ano = 2024

# "Ola Mundo, Gonçalo em 2024"

#str(ano) converte para string

print("Ola mundo, " + nome + " em " + str(ano))

print("Ola mundo,", nome  ,"em", ano)

print(f"Ola Mundo, {nome.upper()} em {ano}")

# %

op2 = 10 % 3
print(op2)


op2 = 12 % 3
print(op2)


op2 = 10 / 3
print(op2)


op2 = 10 // 3
print(op2)


# ler dados do teclado
nome2 = input("Digite seu nome: ")
print(f"ola, {nome2}")

print("--" * 10)
#Ifs


idade = 18

if idade > 18:
    print("adulto")
elif idade > 15:
    print("jovem")
else:
    print("criança")
    

# Faça um programa que peça dois numeros e imprima a soma.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2

print(num1,"+",num2, "=" ,soma)

print("Faça um programa que peça as 4 notas bimestrais e mostre a média.")

val1 = float(input("Digite o primeiro número: "))
val2 = float(input("Digite o segundo número: "))
val3 = float(input("Digite o terceiro número: "))
val4 = float(input("Digite o quarto número: "))

media = (val1 + val2 + val3 + val4) / 4

print(media)