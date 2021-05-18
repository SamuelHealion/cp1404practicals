"""
CP1404 Practical 8 - Practice and Extension
Further car classes using the Car class as the parent class
GassGussler uses more fuel than it should
"""

from prac_08.car import Car


class GassGussler(Car):
    """Specialised version of the Car class that uses more fuel than it should."""
    def __init__(self, name, fuel, efficiency):
        """Initialise a GassGussler instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.efficiency = efficiency
        self.effective_efficiency = 1 + efficiency / 100

    def __str__(self):
        """Return a string representation of a GassGussler object"""
        return "{}, fuel={:.2f}, odometer={:.2f} uses {}% more fuel".format(self.name, self.fuel, self.odometer, self.efficiency)

    def drive(self, distance):
        """Drive like parent Car but increase fuel consumption based on efficiency."""
        if distance > self.fuel / self.effective_efficiency:
            distance = self.fuel / self.effective_efficiency
            self.fuel = 0
        else:
            self.fuel -= distance * self.effective_efficiency
        self.odometer += distance
        return distance


def run_tests():
    """Test the GassGussler class."""
    car = GassGussler("Ol'Thirsty", 100, 100)
    print(car)
    car.drive(30)
    print(car)


if __name__ == '__main__':
    run_tests()
