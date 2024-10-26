from Quadrado import Quadrado
from triangulo import Triangulo
from trapezio import Trapezio
from circulo import Circulo

q1 = Quadrado(20, "Amarelo")

q2 = Quadrado(34, "Azul")

"""
Criar base da para a class

triangulo
circulo
trapezio

""" 

# Triangulos
t1 = Triangulo(20, 15, "Amarelo")

t2 = Triangulo(32, 18, "Azul")

# Trapezios
t3 = Trapezio(20, 13, 19, "Vermelho")

t4 = Trapezio(15, 24, 31, "Roxo")

#Circulo
c1 = Circulo(27, "Verde")

c2 = Circulo(12, "Laranja")


"""
1 - Crie 4 Quadrados
2 - Indique o que tem maior area


"""

q3 = Quadrado(8, "Amarelo")
q4 = Quadrado(7, "Azul")
q5 = Quadrado(3, "Verde")
q6 = Quadrado(5, "Vermelho")

q3_area = q3.area()
q4_area = q4.area()
q5_area = q5.area()
q6_area = q6.area()

quadrados = [q3_area,q4_area,q5_area,q6_area]

tamanho = 0
quadrado = 0
for maior in quadrados:
    if maior > tamanho:
        tamanho = maior
    quadrado += 1


print(f"Área do quadrado 1 (Amarelo): {q3_area}")
print(f"Área do quadrado 2 (Azul): {q4_area}")
print(f"Área do quadrado 3 (Verde): {q5_area}")
print(f"Área do quadrado 4 (Vermelho): {q6_area}")

print(f"O quadrado com a maior área é o quadrado {quadrado}, com uma área de {tamanho}.")