from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):
    isOn = False
    
    def move(self):
        print('Car hereket etdi')
    
    def start(self):
        self.isOn = True

class Horse:
    
    def move(self):
        print('At hereket etdi')

class Motocycle(Vehicle):
    isOn = False
    
    def move(self):
        print('Motocycle hereket etdi')
    
    def start(self):
        self.isOn = True


def move_vehicle(vehicle):
    vehicle.start()
    vehicle.move()

bmw = Car()
mc = Motocycle()
at = Horse()

move_vehicle(bmw)
move_vehicle(mc)
move_vehicle(at)

