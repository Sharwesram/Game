class vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage

class bus(vehicle):
    def __init__(self, max_speed, mileage,veh):
        self.veh=veh
        super().__init__(max_speed, mileage)
a=bus(120,100,"School Volvo")
print(a.veh,a.max_speed,a.mileage)

class person:
    def __init__(self,name,id_num):
        self.name=name
        self.id_num=id_num
    def display(self):
        print(self.name)
        print(self.id_num)
class employee(person):
    def __init__(self, name, id_num,salary,post):
        super().__init__(name, id_num)
    def display(self):
        print(f"Name:{self.name},ID Number:{self.id_num}")
   


b=employee("Sharwesram . K . S",57,10000,"Chennai")
b.display()

class bird:
    def __init__(self,name,c):
        self.name=name
        self.c=c
    def wit(self):
        print(f"Name of the bird is {self.name}")
    def swim(self):
       if self.c=="yes".upper():
          print(f"{self.c} I can swim.")
       else:
           print(f"{self.c} I can't swim.")
class penguin(bird):
    def __init__(self, name, c):
        super().__init__(name, c)


c=penguin("Penguin","YES")
c.wit()
c.swim()

        