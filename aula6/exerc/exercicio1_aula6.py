"""
Crie uma app que peça ao utilizador os seus dados e
guarde esses dados num ficheiro de texto

deve utilizador o try/except para evitar errros
"""

try:
    nome = input("Por favor, introduza o seu nome: ")
    idade = input("\nPor favor, introduza a sua idade: ")
    morada = input("\nPor favor, introduza a sua morada: ")
    telefone = input("\nPor favor, introduza o seu número de telefone: ")

    file = open("dados_utilizador.txt", "w")
        
    file.write(f"Nome: {nome}\n")
    file.write(f"Idade: {idade}\n")
    file.write(f"Morada: {morada}\n")
    file.write(f"Telefone: {telefone}")
    
    print("\nDados guardados com sucesso!")

except Exception as e:
    print(f"\nOcorreu um erro inesperado: {e}")