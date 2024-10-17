# Crie a função -> sum_lista <-  que some todos os valores de uma lista de inteiros

def sum_lista(lista) -> int:
    return sum(lista)

list1 = [1, 2, 3, 4, 5]
result = sum_lista(list1)
print(f"Sum of the list {list1}: {result}")