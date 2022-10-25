import math

class Animal:

    def __init__(self, species, age, offense, defense,nature):

        self.species=species
        self.age=age
        self.offense=offense
        self.defense=defense
        self.nature=nature

    def info(self):
        print(f'{self.species}is {self.age} years old, has {self.offense} offense, {self.defense} defense, and has a {self.nature} nature.')

animals=[

    Animal("Lion",  4,  900,  800, "brave"),
    Animal("Wolf",  3,  500,  300, "calm"),
    Animal("Bear",  6, 1200, 1000, "gentle"),
    Animal("Tiger", 5, 1500, 1300, "smart")

]

for A in animals:
    A.info()

# L.print()
# W.print()
# B.print()
# T.print()

# b[0].species
# b[0].age
# b[0].offense
# b[0].defense
# b[0].nature

# def output(self):
#     print(f'{self.species}is {self.age} years old, has {self.offense} offense, {self.defense} defense, and has a {self.nature} nature.')
