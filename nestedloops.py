# a=str(input("Enter a string:"))
# b=str(input("What letter to find:"))
# c=0
# i = 0
# while i < len(a):
#     if a[i] == b:
#         c += 1
#     i += 1

         

# print(c)

# a=int(input("Enter the highest value:"))
# b=int(input("Enter the lowest value:"))
# c=0
# pc=0
# for i in range(b,a+1):
#     if i > 1:
#        for i1 in range(2,i):
#             if i%i1==0:
#                break
#        else:
#          print(i)

    
#     # if c<2:
#     #    pc += 1
#     #    print(i)

# print(f"There are {pc} prime numbers between {a} and {b}.")

a=input("Enter a number:")
l=len((a))
if l%2!=0:
    s=l//2
    print((a[s]))
else:
    s2=(l-1)//2
    s1=(l)//2
    print(a[s2],",",a[s1])
