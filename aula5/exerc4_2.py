"""
Faça uma função para imprimir, deve receber como parametro o numero de niveis:

1
1 2
1 2 3
1 2 3 4

------------------

1 2 3 4 5 6 7 8  ... 8 vezes

"""

def piramide2(z: int):
    print("-"*15)
    print("Piramide criada: ")


    for i in range(1, z + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
        
    print("-"*15)

y = int(input("Insira um numero: "))
piramide2(y)