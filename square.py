import math

square=[]
e=[]
o=[]

sr=int(input("Enter the begining range:"))
er=int(input("Enter the ending range:"))
for i in range(sr,er+1):
    a=math.sqrt(i)
    if a.is_integer():
        square.append(i)
        if a % 2 == 0 :
            e.append(i)
        else:
            o.append(i)
        
    else:
        pass
print("square numbers availble between the range given is :")
print(square)
print(f"Odd square numbers between {sr} and {er} are:")
print(o)
print(f"Even square numbers between {sr} and {er} are :")
print(e)