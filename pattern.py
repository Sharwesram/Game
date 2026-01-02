# a=int(input("Enter a number:"))
# b=1
# for i in range(a):
#     for i1 in range(i+1):
#         print(b,end="")
#         b = b + 1
#     print()

a=int(input("Enter number of rows:"))
# if a % 2==0:
#     h=a//2
# else:
#     h=(a//2)+1
# s = h - 1
# for i in range(1,h+1):
#     for j in range(1,s+1):
#         print(end=" ")
#     s = s-1
#     b=1
#     for j1 in range(2*i-1):
#         print(end=str(b))
#         b += 1
#     print()
# s = 1
# for i in range(1,h):
#     for j in range(1,s+1 ):
#         print(end=" ")
#     s += 1
#     b=1
#     for i1 in range(1,2*(h-i)):
#         print(end=str(b))
#         b += 1
#     print()
b=1


for i in range(a,0,-1):
   
    for j in range(1,i+1):
        print(end=str(j))
        
        
    print()
        
         