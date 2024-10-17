import random

# Crie uma lista com 1000 números inteiros aleatórios
# Imprima o valor todos os valores da lista multiplicados pela posição
#
# Exemplo:
# lista -> [3,4,5,10]
# output:
# 0
# 4
# 10
# 30

lista = [random.randint(0, 1000)
    for _ in range(4)]
    
for i, valor in enumerate(lista):
    print(i * valor)