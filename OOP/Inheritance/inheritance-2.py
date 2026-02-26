class Vehicle:
    def __init__(self, vehicle_id = None, brand = None):
        self.vehicle_id = vehicle_id
        self.brand = brand
    
    def calculate_rent(self):
        pass


class Car(Vehicle):
    def __init__(self, vehicle_id = None, brand = None, price_per_day = None, days = None):
        super().__init__(vehicle_id, brand)
        self.price_per_day = price_per_day
        self.days = days
    
    def calculate_rent(self):
        return self.price_per_day * self.days


class Bike(Vehicle):
    def __init__(self, vehicle_id = None, brand = None, price_per_hour = None, hours = None):
        super().__init__(vehicle_id, brand)
        self.price_per_hour = price_per_hour
        self.hours = hours

    def calculate_rent(self):
        return self.price_per_hour * self.hours


class Truck(Vehicle):
    def __init__(self, vehicle_id = None, brand = None, price_per_km = None, distance_travelled = None):
        super().__init__(vehicle_id, brand)
        self.price_per_km = price_per_km
        self.distance_travelled = distance_travelled

    def calculate_rent(self):
        return self.price_per_km * self.distance_travelled
    

c1 = Car(12, "Maruti", 20, 3)
b1 = Bike(123, "pulsar", 15, 5)
t1 = Truck(1234, "Benz", 10, 4)


print(c1.calculate_rent())
print(b1.calculate_rent())
print(t1.calculate_rent())