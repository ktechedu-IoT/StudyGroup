import random as ran

class Animal:
    def __init__(self,name,age,attack,deffence,character):
        self.name = name
        self.age = age
        self.attack = attack
        self.deffence = deffence
        self.character = character

    def info(self):
        print(f"{self.name}의 나이는 {self.age}살 이고, 공격력은 {self.attack}이며, 방어력은 {self.deffence}이고, 성격은 {self.character}")

wolf = Animal("늑대", 4, 200, 100, "따뜻하다")
turtle = Animal("거북이", 50, 10, 200, "여유롭다") 
rabbit = Animal("토끼", 1, 30, 50, "급하다")
cat = Animal("고양이", 7, 50, 70, "까칠하다")

wolf.info()
turtle.info()
rabbit.info()
cat.info()