class roman_converter:
    inti={1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
    NUM=int(input("Enter a number:"))
    print(f"{NUM}={inti[NUM]}")
OB=roman_converter()