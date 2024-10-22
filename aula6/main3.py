

file = open("demo.txt", "wt")


file.write("Linha 4\n")
file.write("Linha 5\n")
file.write("Linha 6\n")




print("Done")


"""
Crie uma app que peça ao utilizador os seus dedos e
guarde esses dados num ficheiro de texto

deve utilizador o try/except para evitar errros

"""

myInfo = open("infos.txt", "at")
myInfo.write("-----------------------------\n")
nome = input("Nome: ")
idade = input("Idade: ")
email = input("Email: ")

myInfo.write(f"Nome: {nome}\nIdade: {idade}\nEmail: {email}\n")

myInfo.close()