"""

1 - Crie um dicionário com os seus dados: nome e turma
2- Usando o dicionário criado recentemente, imprima o seu nome
3- Adiciona a sua localidade
4- Mostre a msg:

"Ola, o meu nome é <Nome>, sou de <Localidade> e estou na turma <Turma>."


"""

info = {"nome": "turma","localidade": "" }

info["nome"] = "Daniel"

print(info["nome"])

info["turma"] = "PIPL0923"

info["localidade"] = "Alcochete"

print(f"Ola, o meu nome é {info['nome']}, sou de {info['localidade']} e estou na turma {info['turma']}.")