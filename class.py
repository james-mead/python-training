"""Example of using classes with Python."""


class User:
    """User class."""

    name = ""

    def __init__(self, name):  # initialize User with constructor
        self.name = name
        print("Object created wih the name " + str(self.name))

    def printName(self):
        print(self.name)


class Manager(User):
    """Manager class."""

    def giveWork(self):
        """Give work."""
        print("Gives Work")


james = User("James")
james.printName()
Charmian = Manager("Charmian")
Charmian.giveWork()
