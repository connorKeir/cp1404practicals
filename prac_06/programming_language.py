"""CP1402 practical - programming language """

class ProgrammingLanguage:
    """represents a programming langauge object"""
    def __init__(self, typing, reflection, year):
        """Initialise a Programming language instance"""

        self.typing = typing.Title()
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == 'Dynamic':
            return True
        else:
            return False


