# Родительский класс Animal
class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

# Класс наследник Mammal
class Mammal(Animal):
    pass


# Класс наследник Predator
class Predator(Animal):
    pass


# Класс наследник Plant
class Plant:
    def __init__(self, name, edible = False):
        self.name = name
        self.edible = edible


# Класс наследник Flower
class Flower(Plant):
    pass


# Класс наследник Fruit
class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

# Создание объектов классов
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Проверка атрибутов и выполнение действий
print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)