class Car:
    def __init__(self, car_id, name, price, status):
        self.car_id = car_id
        self.name = name
        self.price = price
        self.status = status

    def introduce(self):
        print(f"Car ID: {self.car_id} \nCar name: {self.name} \nPrice: {self.price} euros\nStatus: {self.status}")
    
    def mark_as_sold(self): 
        self.status = "sold"