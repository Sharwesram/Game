import datetime
try:
    d=int(input("Enter your date of BOD :"))
    m=int(input("Enter the number of the month:"))
    y=int(input("Enter the year of your BOD :"))
    td=datetime.date.today()
    ye=td.year
    ym=td.month
    
    
    n=1,3,5,7,8,10,12
    n2=4,6,9,11
    if m in n and d < 32:
        pass
    
    elif m==2 and y % 4 == 0 and d < 30:
        pass
    
    elif m in n2 and d < 31 :
        pass
    else:
        print("Invalid BOD !")
        quit()
    
    
    if ym==m:
        age=ye-y
    else:
        age=(ye-y)-1
    print("your age is "+str(age))
    if age % 2 == 0 :
        print("Your age is an even number !")
    else:
        print("Your age is an odd number !")

    

except ValueError as v:
    print("An Error Has Occured, Enter Valid BOD:","\n",v)