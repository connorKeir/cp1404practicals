"""
CP1404 Practical
Car class - Taxi Class - SilverServiceTaxi Class
"""
from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that allows for different price_per_km"""

    flagfall = 4.50

    def __init__(self, name="SilverServiceTaxi", fuel=0, fanciness=2):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.price_per_km = self.price_per_km * fanciness

    def get_fare(self):
        """Return the price for the SilverServiceTaxi trip."""
        normal_fare = super().get_fare()
        return normal_fare + self.flagfall

    def __str__(self):
        """Return a string like a Taxi but with flagfall."""
        return "{} plus a flagfall of ${:.2f}".format(super().__str__(), self.flagfall)


