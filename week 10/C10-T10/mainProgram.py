from car import Car

cars = []
cars.append(Car("101", "Volkswagen Golf", "25000", "available"))
cars.append(Car("102", "BMW M3", "60000", "available"))

print("Current cars for sale: \n")
for car in cars:
    car.introduce()
    print("\n")

soldID = input("Enter the ID of the car you want to mark as sold: \n")
print("Updated car list: \n")
for car in cars:
    if car.car_id == soldID:
        car.mark_as_sold()
    car.introduce()
    print("\n")