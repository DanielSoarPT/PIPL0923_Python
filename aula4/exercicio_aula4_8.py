"""

Faça uma função para imprimir:
    a altura deve ser recebida como parametor
    
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n   ... n

    """
    
def ex_8(altura: int):
    for i in range(1, altura + 1):
        print(f"{i} " * i)

print("Imprimar com altura 8:")
ex_8(8)