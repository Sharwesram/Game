# def totslcalc(ba,tp):
#     ta=ba*tp/100
#     sum=ta+ba
#     print("Tip amount =",ta)
#     print("total bill = ",sum)
# ba=float(input("Enter the bill amount:"))
# tp=float(input("Enter the tip percentage:"))
# totslcalc(ba,tp)
    
# def cube(num):
#     return num**3

# def div(num):
#     if num % 3 == 0 :
#         return cube(num)
#     else :
#         return False
# print(div(10))

def fact(n):
    if n == 0 or n==1:
      return 1 
    else:
        return n*fact(n-1)
print(fact(3))