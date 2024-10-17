# Crie uma função que conte quantas vezes as palavras aparecem numa string

def contarpalavras():
    frase = input("Digite uma frase: ")
    palavras = frase.split()
    contagem = {}
    for palavra in palavras:
        palavra = palavra.lower()
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1

    print("Contagem de palavras:")
    for palavra, conta in contagem.items():
        print(f"{palavra} - {conta}")


contarpalavras()