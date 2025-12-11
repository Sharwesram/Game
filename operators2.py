# num=10
# if num>0:
#     print("positive number")

# else:
#     print("negative number")

# a=100
# s=120
# if a<s:
#     b=s-a
#     print(f"It is profit by {b} rupees")

# else:
#     print("It is loss")

# a=int(input("Enter a number:"))
# if a>15:
#     print("It is greater than 15")
#     b=a-15
#     print(f"It is greater by {b}")

# else:
#     print("It is smaller than 15")
#     c=15-a
#     print(f"It is smaller by{c}")

# print("Thank you")

# a=int(input("Enter a number:"))
# if(a/):
#     print("it is an even number")

# else:
#     print("it is an odd number")
num=11
if num > 1:
   for i in range(2, num):
       if num % i == 0:
          print(num, "is not a prime number")
          break
   else:
       print(num, "is a prime number")

else:
   print(num, "is not a prime number")