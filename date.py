import datetime
import calendar
import random
import time
# print(datetime.datetime.now())

# s="1/1/2025"
# e="1/1/2026"
# fo="%m/%d/%Y"
# st_date=int(time.mktime(time.strptime(s,fo)))
# end_date=int(time.mktime(time.strptime(e,fo)))

# r=random.randint(st_date,end_date)

# a=time.strftime(fo,time.localtime(r))

# print(a)

class exp:
   
    def __init__ (self):
       pass
    def expenditure(self,e,h,p,v):
       self.e=e
       self.h=h
       self.p=p
       self.v=v
       n=int(input("Number of days stayed in hotel:"))
       print(f" Total cost spent for staying in hotel = ${h*n}")
       e += (h*n)
       print(f"Cost spent for plane including both from and return trip = ${p*2}")
       e += (p*2)
       d=int(input("Enter the number of days the vehicle was rented:"))
       print(f"Cost spent for renting vehicle during the trip = ${v*d}")
       e += (v*d)
       return(f"Your total expenditure for the trip = ${e}")
    
o=exp()


print(o.expenditure(0,150,500,200))
