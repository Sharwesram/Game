num=int(input("Enter a number:"))
bn=""
while num>0:
    bn += str(num % 2)
    num //=2

print(bn[::-1])

num1 = float(input("Enter a fraction: "))
b = "0."
while num1 > 0 :
    num1 *= 2
    fi=int(num1)
    b += str(fi)
    if fi == 1:
        num -= 1
        if num1==0:
           print(b)
           break
    d=0
    
    s=0
    if num1 == int(num1):
       print(b)
       break


       
        