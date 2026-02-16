class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self,radius,pie):
        print(f"Area of the circle={pie*(radius*radius)}")
    def perimeter(self,radius,pie):
        print(f"Perimeter of the circle={(2*pie)*radius}")

r=float(input("Enter the radius of the circle:"))
p=22/7
ob1=circle(r)
ob1.area(r,p)
ob1.perimeter(r,p)