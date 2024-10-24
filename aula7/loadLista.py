from Pessoa import Pessoa
import pickle

myData = "Dados"

with open("saveList.pickle", "rb") as f:
    myData = pickle.load(f)
    

print(myData)