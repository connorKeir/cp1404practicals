"""CP1402 practical - programming language """


class ProgrammingLanguage:
    """represents a programming langauge object"""

    def __init__(self, name, typing, reflection, year):
        """Initialise a Programming language instance"""

        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == 'Dynamic':
            return True
        else:
            return False

    def __str__(self):
        return"{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                          self.year)
