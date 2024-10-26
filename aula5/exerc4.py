"""
Faça uma função para imprimir, deve receber como parametro o numero de niveis:

1
2 2
3 3 3
4 4 4 4

n n n n n n  ... n vezes

"""

def piramide(x):
    
    for i in range(1, x + 1):
        print(f"{i} " * i)
        
y = int(input("Insira um numero: "))
piramide(y)

