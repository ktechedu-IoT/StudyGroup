import math

class Animal:

    index=0
    def __init__(self, species=" ", age=" ", offense=" ", defense=" ",nature=" "):

        self.species=species
        self.age=age
        self.offense=offense
        self.defense=defense
        self.nature=nature
        self.data=[]

    def __str__(self):
        return self.species + " "  + self.age + " " + self.offense + " " + self.defense + " " + self.nature
    def __repr__(self):
        return self.__str__()

    def join(self):
        
        for i in range(2):
            species=input("What's animal?")
            age=input("How old???")
            offense=input("?")
            defense=input("?")
            nature=input("How?")
            animal=Animal(species, age, offense, defense, nature)
            self.data.append(animal)
            print(self.data)
        print(self.data)
    
    def find(self):

        #animal=("species", " ", " ", " ", " ")
        name=input(" ?????? ")
        for a in self.data:
            if a.species==name:
                print(a)
x=Animal()
x.join()
x.find()
