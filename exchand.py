# try:
#     a=int(input("Enter a number:"))
#     print(a)
# except ValueError as V:
#     print("Exception",V)
    
# try:
#     a=int(input("Enter a Number:"))
#     b=int(input("Enter a Number:"))
#     print(a/b)
# except ZeroDivisionError as d :
#     print("Exception:",d)
# except SyntaxError as s:
#     print("Exception:", s)
# else:
#     print("Done!")
# finally:
#     print("Executed!")

# try:
#    a=int(input("Enter a number:"))
#    while a > 0 :
#         while a % 2 == 0 :
#             print("Bye !")
#         a -= a
      
# except Exception:
#    print("Error !")
# else:
#     print("Not divisible by 2")
# finally:
#    print("Executed !")

valid=False
while not valid:
    try:
        a=int(input("Enter num:"))
        while a % 2 == 0 :
            print("bye!")
        valid=True
    except ValueError as e:
        print("Exception",e)