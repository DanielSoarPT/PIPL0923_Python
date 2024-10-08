
#receba 5 valores como input e adicione esses valores a uma lista
#mostre o conteudo da lista 
print("-------"* 10)
nova_lista = ["um", "dois", "tres", "quatro", "cinco"]

for i in range(5):
    novos = input("Digite um valor: ")
    nova_lista.append(novos)
    
print("\nLista com os valores adicionados: ")
print(nova_lista)


#receba N valores como input e adicione esses valores a uma lista
#mostre o conteudo de lista
#deve perguntar ao utilizador quando valores pretende adicionar
print("-------"* 10)
lista = []

n = int(input("Quantos valores você deseja adicionar à lista? "))

for i in range(n):
    valor = input(f"Digite o valor {i + 1}: ")
    lista.append(valor)

print("Conteúdo da lista:", lista)

#Faça um Programa que leia 20 numeros inteiros e armazene-os numa lista
#Armazene os numeros pares na lista PAR e os numeros IMPARES na lista impar
#Imprima os 3 vetores

print("------" * 10)
numeros = []
PAR = []
IMPAR= []

for i in range(20):
    num = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(num)
    
    if num % 2 == 0:
        PAR.append(num)
    else:
        IMPAR.append(num)

print("Lista de números:", numeros)
print("Lista de números pares:", PAR)
print("Lista de números ímpares:", IMPAR)



#receba N notas (0 a 20) como input e adicione esses valores a uma lista
#mostre o conteudo de lista
#deve perguntar ao utilizador quando valores pretende adicionar
#deve garantir que todas as notas sao validas
#deve assumir que o utilizador vai tentar adicionar valores numericos

print("-------" * 10)
num = int(input("Numeros de notas:"))
lista = []

for i in range(num):
    while True:
            nota = float(input(f"nota {i+1} (0 a 20): "))
            if 0 <= nota <= 20:
                lista.append(nota)
                break
            else:
                print("Nota inválida. Inserir um valor de 0 a 20")
 
    
for n in lista:
    print(f"{n:.2f}")


'''
#Faça um Programa que leia 20 numeros inteiros e armazene-os numa lista
#Armazene os numeros pares na lista PAR e os numeros IMPARES na lista impar
#Imprima os 3 vetores
lista = [1,3,3,1,123,31,23,1234,54,6,25,1,4,42,5,62,4,134,414,3,45,1,413,234,532]

par = [ n for n in lista if n % 2 == 0]
impares = [ n for n in lista if n % 2 != 0]

print(f"par : {par}")
print(f"Impares: {impares}")
'''