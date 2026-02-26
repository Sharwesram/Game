class BMW:
    def __init__(self,ft,ms):
        self.ft=ft
        self.ms=ms
    def fuel_type(self):
        print(f"The fuel type of the car BMW is {self.ft}.")
    def max_speed(self):
        print(f"The maximum speed of the car BMW is {self.ms}km/h.")
class Ferrari:
    def __init__(self,ft,ms):
        self.ft=ft
        self.ms=ms
    def fuel_type(self):
        print(f"The fuel type of the car Ferrari is {self.ft}.")
    def max_speed(self):
        print(f"The maximum speed of the car Ferrari is {self.ms}km/h.")
bmw=BMW("Diesel",300)
ferrari=Ferrari("Deisel",400)
for cars in (bmw,ferrari):
    cars.fuel_type()
    cars.max_speed()