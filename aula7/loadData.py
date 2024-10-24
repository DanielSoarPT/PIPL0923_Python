from Pessoa import Pessoa
import pickle

print("--- Faz o Load dos Dados ---")

#le de bin
file2 = open("Pessoa.pickle", "rb")
p2 = pickle.load(file2)
print(p2)