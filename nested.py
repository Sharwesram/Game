# per=23
# mc="Yes"
# if per > 75 :
#     print("Allowed")

# else:
#     if mc=="Yes":
#        print("Allowed")

#     else:
# #         print("not allowed")
# u=int(input("Enter the amount of units:"))
# if u < 50 :
#     print("amount charged=",(u*2))
    
# elif u>=50 :
#     print("amount charged=",(u*3))
#     if u<100 :
#         print("Amount charged=",(u*5))
#     else:
#         print("amount charged=",(u*8))
print("1.Bike","\n","2.Car")
a=int(input("1 OR 2"))
if a==1:
    print("You have chosen Bike.")
    b=int(input("In which bike do you want to go 1.Superbike or 2.sports bike 1 or 2:"))
    if b==1 :
        print("You have chosen superbike.")
        sb=int(input("You want kawasiki ninja H24 or SUZUKI. 1 or 2"))
        if sb==1:
           print("you have chosen Kawasiki ninja h24.")
        elif sb==2:
            print("you have chosen suzuki bike.")
        
    elif b==2:
        print("You have chosen sportsbike.")
        spb=int(input("You want yamaha or honda. 1 or 2:"))
        if spb==1:
            print("You have chosen yamaha.")
        elif spb==2:
            print("You have chosen honda.")
elif a==2:
    print("You have chosen Car.")
    b1=int(input("In which bike do you want to go 1.racingcar or 2.normal car 1 or 2:"))
    if b1==1 :
        print("You have chosen racing car.")
        sb1=int(input("You want BMW or SUZUKI. 1 or 2"))
        if sb1==1:
           print("you have chosen BMW.")
        elif sb1==2:
            print("you have chosen suzuki car.")
        
    elif b1==2:
        print("You have chosen normal car.")
        spb1=input("You want mahindra or honda. 1 or 2:")
        if spb1==1:
            print("You have chosen mahindra.")
        elif spb1==2:
            print("You have chosen honda.")