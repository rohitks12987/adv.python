class vehicle:
  def start(self):
    print("Vehicle Start")
class car(vehicle):
  def start (self):
    super().start()
    print("Car starts by Key")
class bike(vehicle):
  def start(self):
    super().start()
    print("bike stars by kick")   
class scotty(vehicle):
  def start (self):
    super().start()
    print("Scotty starts by switch")
c = car()
c.start()
print()
b = bike() 
b.start()