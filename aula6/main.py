"""

txt

bin


"""

"""

r - read
w - write
a - append

x - cria

t - txt
b - bin

"""

l = [1,2,3]

def myFunc(n):
    
    if n == 0:
        Exception("n Nao pode ser 0")
        
    print("myFunc - it Works !!")



try:
    
    myFunc(4)
    print(l[9])
    file = open("demo.txt", "xt")
    
except FileExistsError as e:
    print(f"O file ja existe - {e.filename}")
    
except IndexError as e:
    print(f"IndexError: list index out of range - {e}")

except Exception as e:
    print(e)
    
print("it works!!")