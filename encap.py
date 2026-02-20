# class var:
#     __a=1
#     def __init__(self):
#         self.__var1=10
#         self.__var2="Hello World !"
#     def hello(self):
#         print(self.__var1)
#     def __meth():
#         print("Private!")
# ob1=var()
# ob1.hello()
# print(ob1.__a)
# ob1.__meth()

# class computer:
    
#     def __init__(self):
#         self.__maxprice=50000
#     def sell(self):
#         print("The cost of selling price is rupees 40000")
#     def set_max_price(self):
#         self.__maxprice += 40000
#         print(self.__maxprice)
    
# ob2=computer()
# ob2.sell()
# ob2.set_max_price()

class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def dis(self):
        print(f"({self.x},{self.y})")
ob3=point(5,7)
ob3.dis()        
