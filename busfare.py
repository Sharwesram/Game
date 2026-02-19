class vehicle:
    
    
    def __init__(self,cost,per,nop,fare,per_value):
        self.cost=cost
        self.per=per
        self.nop=nop
        self.fare=fare
        self.per_value=per_value
    
    def cal(self):
        self.fare += (self.cost*self.nop)
    def percentage(self):
        self.per_value += 1+(self.per/100)
        self.fare *= self.per_value
    def print_total_fare(self):
        print(f"Total fare of the bus is RUPEES {self.fare}")
class bus(vehicle):
    def __init__(self, cost, per, nop, fare, per_value):
        super().__init__(cost, per, nop, fare, per_value)
ob1=bus(100,10,50,0,0)
ob1.cal()
ob1.percentage()
ob1.print_total_fare()

