# Crie um dicionário dinâmico, onde pergunta ao utilizador quantos valores quer adicionar.
# Em seguida deve pedir ao utiliazdor os dados as keys e valores que quer adicionar e adicionar os respetivos valores


dicionario = {}

num_pares = int(input("Quantos pares chave-valor você quer adicionar ao dicionário? "))

for i in range(num_pares):
    chave = input(f"Digite a chave {i+1}: ")
    valor = input(f"Digite o valor para a chave '{chave}': ")
    dicionario[chave] = valor

print("\nDicionário:")
print(dicionario)