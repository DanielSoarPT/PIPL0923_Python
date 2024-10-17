
def ola_mundo():
    print("Ola mundo")
    
ola_mundo()

# Ola mundo, 2024

def ola_mundo2():
    print("Ola mundo, 2024")
    
ola_mundo2()

def ola_mundo_v2(nome):
    print(f"Ola mundo, {nome}")
    
ola_mundo_v2("Daniel")
ola_mundo_v2("Rui")
ola_mundo_v2("Ana")

num = 12



def ola_mundo_v3(nome: str, ano: int, idade: int):
    print(f"Ola mundo, {nome}, {ano}")
    
    
ola_mundo_v3("Daniel", 2000, 88)


def soma(valor1:int, valor2:int):
    return valor1 + valor2


res = soma(3, 4)
print(res)


res2 = soma(3.5, 4.5)
print(res2)

res3 = soma("3.5", "4.5")
print(res3)



# Crie uma função que some todos os valores de uma lista de inteiros

def sum_lista(lista) -> int:
    return sum(lista)

list1 = [1, 2, 3, 4, 5]
result = sum_lista(list1)
print(f"Sum of the list {list1}: {result}")
