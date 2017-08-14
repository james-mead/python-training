class Cat:

    def __init__(self, name="Unknown", weight=0, height=0):
        self.name = name
        self.weight = weight
        self.height = height

    def run(self):
        print("{} the cat likes to run".format(self.name))


def main():

    ninga = Cat("Ninga", 12, 20)
    ninga.run()

main()