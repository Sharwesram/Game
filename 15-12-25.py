c=input("Enter a alphabet:")
a=("abcdefghijklmnopqurstuvwxyz")
b=("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def lowercase() :
    if c in a :
       cp=a.index(c) 
       vc=cp + 1
       asc=96 + vc
       print(f"The ASCII code of {c} is {asc}.")


def uppercase():
    if c in b :
        cb=b.index(c)
        vb=cb+1
        asb=64+vb
        print(f"The ASCII code of {c} is {asb}.")






if c in a :
   lowercase()

elif c in b:
   uppercase()

else:
   print("Invalid alphabet !")