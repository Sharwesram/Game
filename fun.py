# def wellwishes(name):
#     print("Hello, How are you ?")
#     return name
# print(wellwishes("Sharwesram"))

# def wheather(w):
#     print(w)

# w=str(input("Enter the wheather:"))

# wheather(w)


# def add(n1,n2):
#     print("Sum=",n1+n2)
# def sub(n1,n2):
#     print("difference=",n1-n2)
# def mul(n1,n2):
#     print("product=",n1*n2)
# def div(n1,n2):
#     print("quotient=",n1/n2)

# n1=float(input("Enter num 1:"))
# n2=float(input("Enter num 2:"))
# f=int(input("1.ADD 2.SUB 3.MUL 4.DIV. 1or2or3or4:"))
# if f==1: 
#     add(n1,n2)
# elif f==2: 
#     sub(n1,n2)
# elif f==3: 
#     mul(n1,n2)
# elif f==4: 
#     div(n1,n2)

def ff (n) :
    
    if n == 0 or n==1:
        return 1
    else:
        return n*ff(n-1)
n=int(input("Enter a number:"))
print(ff(n))


