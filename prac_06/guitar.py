"""CP1402 - guitar Class"""


class Guitar:
    """represents a guitar object"""

    current_year = 2020

    def __init__(self, name="", year=0, cost=0):
        """initialises a guitar instance"""

        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """prints a instance"""

        return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """returns the age of the guitar object"""

        return self.current_year - self.year

    def is_vintage(self):
        """Determine if instance is vintage"""

        if self.get_age() <= 50:
            return True
        else:
            return False
