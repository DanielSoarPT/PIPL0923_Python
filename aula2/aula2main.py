#Condições / Controlo de fluxo

#boolean

'''

T e T -> T
T e F -> F
F e T -> T
F e F -> F




T ou T -> T
T ou F -> T
F ou T -> T
F ou F -> F


T xou T -> F
T xou F -> T
F xou T -> T
F xou F -> F



'''

ano = 2024


# if (se)
if ano == 2024:
    print("ano = 2024")
else:
    print("Outro ano")

print("fora do if")

#Faça um programa que peça dois númros e imprima o maior deles

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print("O", num1, "é  o maior deles ")
else:
    print("O", num2, "é o maior deles ")


print("--" * 10)

num = 5

# F e T -> F
# num = 5
# F       and     T
if num % 2 == 0 and num % 5 == 0:
    print("par e div por 5")

else:
    print("impar ou não divisivel por 5")


'''
== <- comparações 


= <- atribuição

'''


# else if ( se não se )

print("------" * 3)

num = 3
if num  % 2 == 0:
    print("par ou div por 5")
elif num % 5 == 0:
    print("div por 5")
else:
    print("impar nem nao div por 5")
    
# Faça um programa que verifique se uma letra digitada é "F" ou "M",
# Conforme a letra escrever:
# F - Feminino
# M - Masculino
# Genero Invalido


# else ( se não)
letra = input("Digite 'F' ou 'M' conforme o seu género: ")

if letra == "F" or letra == "f":
    print("Feminino")
elif letra == "M" or letra == "m":
    print("Masculino")
else:
    print("Género Inválido")


# switch ( escolha )

num = 0

match num:
    case 0:
        print("o num é 0")
    
    case 1:
        print("o num é 1")
        
    case 5:
        print("o num é 5")

    case _:
        print("Outro valor")
        
        
menu = """######## Menu ########
# op1 ............ 1 #
# op2 ............ 2 #
# op3 ............ 3 #
######################"""

print(menu)

op = input("Selecione a op: ")

match op:
    case "1":
        print("o num é 1")
    
    case "2":
        print("o num é 2")
        
    case "3":
        print("o num é 3")

    case _:
        print("op Invalida")


# loop

#while ( enquanto - faça)

count = 0
while op != "q":
    
    print(f"loop: {count}")
    
    op = input("Selecione a op while: ")
    
    count += 1

num = 0

while num < 10:
    print(num)
    num += 1

'''
num += 1

num++

num = num + 1



num += 4
num = num + 4


num *= 4
num = num * 4



'''

# Range

range(0,10,2)

"""
range(a,b,c)

a - LB

b - UB

c - step, se oculto c = 1

range(1,5)
1, 2, 3, 4

range(5)
0, 1, 2, 3, 4

range(0, 11, 2)
0, 2, 4, 6, 8, 10


"""
    
print("---" * 10)

for elm in range(0, 100):
    if elm % 2 == 0:
        continue
    
    
    print(elm)
    # if elm == 50:
    # break

print("---" * 10)
print("---" * 10)

nomes = [
    "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Julia", "Daniela",
    "Karla", "Lucas", "Mariana", "Nicolas", "Daniela", "Olivia", "Pedro", "Quintino", "Rafael", "Sara", "Tatiana", "Daniela",
    "Ursula", "Vinicius", "Wagner", "Xavier", "Daniela", "Yasmin"
]
    
    
for nome in nomes:
    print(nome)
    
print("Fim do loop")
    
print(nomes.count("Daniela"))
    

print(nomes.__len__())
print(len(nomes))

print(nomes.__contains__("Sara"))
print(nomes.__contains__("Ana"))
print("Pedro" in nomes)

# nomes.sort(reverse=True)

print("-----------" * 5)
nomes.sort()
print(nomes)

"""

var
tipos de dados
type cast - int("..."), srt(...)
tuplos
op com var
if
elif
else
and / or
match
while
for
list
    
"""
"""

Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

"""

nota = input("Introduza uma nota entre 0-10: ")
condicao = nota.isdigit()
while not (condicao and float(nota) >= 0 and float(nota) <= 10):
    print("Nota Inválida")
    nota = input("Introduza uma nota entre 0-10: ")