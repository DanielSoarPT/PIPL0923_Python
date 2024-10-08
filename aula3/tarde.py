# set


from time import sleep
import random

mySet = {"val1", "val2", "val3", "val4"}


print(mySet)

"""
run 1: {'val2', 'val1', 'val3', 'val4'}
run 1: {'val1', 'val2', 'val4', 'val3'}
run 1: {'val1', 'val2', 'val4', 'val3'}
run 1: {'val4', 'val2', 'val1', 'val3'}

"""

#print(mySet[0])

for i in mySet:
    print(i)
    
print("-----"* 3)



mySet = {'val1', 'val2', 'val3', 'val4'}

print(mySet)

mySet.add('val5')

print(mySet)

mySet.add('val3')

print(mySet)



listNum = set()
for _ in range(1000):
    i  = random.randint(0, 1000)
    sleep(0.01)
    listNum.add(i)
    
    

input("continuar? ")
print(listNum.__len__())


print("-----"* 3)
print("-----"* 3)


mySet = {'val1', 'val2', 'val3', 'val4'}

print("val9" in mySet)
mySet.remove("val2")

print(mySet)

mySet.remove("val2")

print("-----"* 3)
print("-----"* 3)

mySet = {'val1', 'val2', 'val3', 'val4'}
mySet2 = {'val5', 'val6', 'val3', 'val4'}

#uniao

print("--- uniao ---"*3)

resp = mySet.union(mySet2)

print(resp)

# intersection

print("--- intersection ---"*3)

resp = mySet.intersection(mySet2)
print(resp)

# dif

print("--- dif ---"*3)

resp = mySet.difference(mySet2)
print(resp)

resp = mySet2.difference(mySet)

# difsym

print("--- symmetric_difference ---"*3)

resp = mySet.symmetric_difference(mySet2)
print(resp)