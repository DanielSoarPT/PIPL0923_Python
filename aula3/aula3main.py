# tuplas

tp1 = ("Gonçalo", "ATEC", 10793)
print(tp1)

print(tp1[0])
print(tp1[1])
print(tp1[2])

#print(tp1[3]) <- Erro

#tp1[0] = "Novo nome" <- Erro

list_temp = list(tp1)
print(list_temp)

list_temp[0] = "Novo nome"
tp1 = tuple(list_temp)

print(tp1)


print("--- unpack ---")

tp1 = ("Gonçalo", "ATEC", 10793)

(nome, escola, UFCD) = tp1

print(nome)
print(escola)
print(UFCD)

nome = "Novo nome 2"


print("--- unpack List ---")
tp1 = ("Gonçalo", "ATEC", 10793)
temp_list = list(tp1)
print(type(temp_list))
(nome, escola, UFCD) = temp_list

print(nome)
print(escola)
print(UFCD)

print("--- metodos tuple ---")
tp1 = ("Gonçalo", "ATEC", 10793, "Gonçalo")
print(tp1.count("Gonçalo"))


# listas (arrays)

# lista vs array



my_list = ["Gonçalo", "Ana", "Rita", "Luis"]

print(my_list)
print(my_list[0])
print(my_list[1])

my_list[0] = "Novo nome"
print(my_list[0])
print(my_list)


print("-----")
nomes = [
    "Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Julia",
    "Karla", "Lucas", "Mariana", "Nicolas", "Olivia", "Pedro", "Quintino", "Rafael", "Sara", "Tatiana",
    "Ursula", "Vinicius", "Wagner", "Xavier", "Yasmin"
]

print(nomes[0])

print(nomes[0:5]) # nomes[n:m] -> n a m-1

print(nomes[6:10]) #nomes[n:m] -> n a m-1

print(nomes[-10: -5])


print(nomes[0:20:3])

nomes.append("Rita")
print(nomes)


nomes.append("Aaron")
print(nomes[-1])

print("insert")
print(nomes[0:4])
nomes.insert(1, "Novo nome")
print(nomes[0:4])

print("remove")

nomes.remove("Novo nome")
print(nomes[0:4])


print(nomes[7])
print(nomes.pop(7))
print(nomes[7])




# print(nomes.remove("Outro nome")) 
# print(nomes.pop(70))

print("For array")

for nome in nomes:
    print(nome)
    
    
# Receba 5 valores como input e adicione esses valores a uma lista.
# Mostre o conteúdo da lista

lista = []

for i in range(5):
    valor = input("Insira cinco valores: ")
    lista.append(valor)

print("Os conteúdos desta lista são:")
print(lista)


# receba N valores como input e adiciona esses valores a uma lista.
# mostre o conteúdo da lista
# deve perguntar ao utilizador quantos valores pretende adicionar

lista2 = []

quantos = int(input("Quantos valores pretende adicionar? "))

for i in range(quantos):
    valor = input("Insira os seus valor: ")
    lista2.append(valor)

print("Os conteúdos desta lista são:")
print(lista2)



# Faça um programa que leia 20 números inteiros e armazene-os numa lista.
# Armazene os números pares na lista PAR e os IMPARES na lista impar.
# Imprima os três vetores.

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

# Receba N notas (0 a 20) como input e adicione esses valores a uma lista
# mostre o conteudo da lista
# deve perguntar ao utilizador quantos valores pretende adicionar
# deve garantir que todas as notas são validas
# deve assumir que o utilizador vai tentar adicionar valores numericos


notas = []

numerosint = int(input("Quantos valores pretende adicionar? "))

for i in range(numerosint):
    while True:
        try:
            nota = float(input("Digite uma nota (0 a 20): "))
            if 0 <= nota <= 20:
                notas.append(nota)
                break
            else:
                print("Nota inválida. Por favor, digite uma nota entre 0 e 20.")
        except ValueError:
            print("Valor inválido. Por favor, digite uma nota numérica.")

print("O conteúdo da lista é:")
print(notas)

# Imprima os três valores

lista = []
quantidade = 20
contagem = 0


while contagem != quantidade:
    leitura = int(input("Insira um valor: "))
    lista.append(leitura)
    contagem += 1
    
par = [n for n in lista if n % 2 == 0]
impar = [n for n in lista if n % 2!= 0]

print("Lista de numeros pares:", par)
print("Lista de numeros impares:", impar)


# Set


# dict