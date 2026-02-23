from abc import abstractmethod
# class base:
#     def dis_val(self):
#         print("value=1")
#     @abstractmethod
#     def task(self):
#         print("ABSTRACT METHOD")
# class sub(base):
#     def task(self):
#         pass
# OB=sub()
# OB.task()
# OB.dis_val()

# class animal:
#     @abstractmethod
#     def pri(self):
#         print("Abstract method")
# class dog(animal):
#     def pri(self):
#         print("Dog")
# ob=dog()
# ob.pri()

class india():
    def __init__(self,c,l,u):
        self.c=c
        self.l=l
        self.u=u
    def dis_cap(self):
        print(f"Capital of our country is {self.c}")
    def dis_l(self):
        print(f"The national language of our country is {self.l}")
    def dis_type(self):
        print(f"The type of our country is {self.u}")
class america:
    def __init__(self,c,l,u):
        self.c=c
        self.l=l
        self.u=u
    def dis_cap(self):
        print(f"Capital of our country is {self.c}")
    def dis_l(self):
        print(f"The national language of our country is {self.l}")
    def dis_type(self):
        print(f"The type of our country is {self.u}")
ob1=india("Delhi","Hindi","Freedom,Peace and Sacrifice")

ob2=america("Washington","English","Development, wealth ")
ob1.dis_cap()
ob1.dis_l()
ob1.dis_type()
ob2.dis_cap()
ob2.dis_l()
ob2.dis_type()