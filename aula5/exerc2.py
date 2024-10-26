from Quadrado import Quadrado

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