class Vehicle:
  def move(self):
    pass
class Bike(Vehicle):
  def move(self):
    print("Bike is a Two Wheeler")
class Car(Vehicle):
  def move(self):
    print("Car is a Four Wheeler")
class Truck(Vehicle):
  def move(self):
    print("Truck is a sixteen Wheeler")
v = [Bike(),Car(),Truck()]
for i in v:
  i.move()