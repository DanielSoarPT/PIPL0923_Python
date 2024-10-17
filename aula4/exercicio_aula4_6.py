# Crie uma função que conte quantas vezes as letras aparecem numa string

# exemplo
# aabbbcccc
#
# output
# a - 2
# b - 3
# c - 4

# exemplo2
# aabbbcccc12c
#
# output
# a - 2
# b - 3
# c - 5

def count_letters(frase: str) -> dict:
    
    contar_letras = {}
    
    for car in frase:
        if car.isalpha():
            contar_letras[car] = contar_letras.get(car, 0) + 1
    
    return contar_letras

frases = ["aaaaaabbbbbbb3ccccccccccc12c"]

for frase in frases:
    print(f"\nInput: {frase}\n")
    result = count_letters(frase)
    for letter, count in result.items():
        print(f"{letter} - {count}")