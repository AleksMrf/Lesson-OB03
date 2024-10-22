# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)
# и методы (`make_sound()`, `eat()`) для всех животных.
#
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы,
# если требуется (например, различный звук для `make_sound()`).
#
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список
# животных и вызывает метод `make_sound()` для каждого животного.
#
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
#
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические
# методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Чирикать"

    def eat(self):
        return f"{self.name} Кушать."


class Bird(Animal):
    def __init__(self, name, age, fly):
        super().__init__(name, age)
        self.fly = fly

    def make_sound(self):
        return "Чирик"


class Mammal(Animal):
    def __init__(self, name, age, habitat):
        super().__init__(name, age)
        self.habitat = habitat

    def make_sound(self):
        return "Ррр"


class Reptile(Animal):
    def __init__(self, name, age, poison):
        super().__init__(name, age)
        self.poison = poison

    def make_sound(self):
        return "Шшш"

class ZooKeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal):
        return f"{self.name} кормит {animal.name}."


class Veterinarian:
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        return f"{self.name} лечит {animal.name}."


def animal_sound(animals):
    for animal in animals:
        print(f"{animal.name} говорит: {animal.make_sound()}")


if __name__ == "__main__":
    swallow = Bird("Ласточка", 2, True)
    lion = Mammal("Лев", 5, "Саванна")
    snake = Reptile("Змея", 3, True)

    animals = [swallow, lion, snake]

    animal_sound(animals)

    zookeeper = ZooKeeper("Егор")
    veterinarian = Veterinarian("Дарья")

    print(zookeeper.feed_animal(swallow))
    print(veterinarian.heal_animal(lion))