# class student:
#     grade2="Grade 2"
#     print(f"Iam in {grade2}")
# ob=student()

# class vehicle:
#     def __init__(self,maxspeed,mileage):
#         self.maxspeed=maxspeed
#         self.mileage=mileage

# ob=vehicle(100,120)
# print(ob.maxspeed)
# print(ob.mileage)

class parrot:
    species="Bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
bird=parrot("Parr",2)
bird2=parrot("Parr2",3)
print(bird2.species)
print(bird.name)
print(bird.age)