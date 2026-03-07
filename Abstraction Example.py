from abc import ABC, abstractmethod

class Appliance(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    def info(self):
        print("This is an electronic appliance")

class WashingMachine(Appliance):

    def turn_on(self):
        print("Washing Machine is ON")

    def turn_off(self):
        print("Washing Machine is OFF")


print("\n----- Abstraction Example -----")
wm = WashingMachine()
wm.info()
wm.turn_on()
wm.turn_off()