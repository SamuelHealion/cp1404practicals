"""
CP1404 Practical 8 - Inheritance
New class inheriting from Taxi class, which in turn inherited from the Car class.
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi class that includes a fanciness value."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness=0.0):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.price_per_km = fanciness * Taxi.price_per_km

    def __str__(self):
        """Return a string like a Taxi but include the flagfall price."""
        return "{} plus flagfall of ${:.2f}"\
            .format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Return the price for the SilverServiceTaxi including the flagfall."""
        return super().get_fare() + self.flagfall
