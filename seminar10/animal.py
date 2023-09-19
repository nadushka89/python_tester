class Animal:
    def __init__(self, name: str, age: int, special: str):
        self._name = name
        self._age = age
        self._special = special

    def get_special(self):
        return self._special


class Dog(Animal):
    def __init__(self, name: str, age: int, **kwargs):
        super().__init__(name, age, kwargs.get('breed', None))


class Cat(Animal):
    def __init__(self, name: str, age: int, **kwargs):
        super().__init__(name, age, kwargs.get('color', None))


class Fish(Animal):
    def __init__(self, name: str, age: int, **kwargs):
        super().__init__(name, age, kwargs.get('habitat', None))

class Humster(Animal):
    def __init__(self, name: str, age: int, **kwargs):
        super().__init__(name, age, kwargs.get('fur_color', None))

class AnimalFactory:
    def create_animal(animal_type: str, name: str, age: int, **kwargs):
        if animal_type == 'Dog':
            return Dog(name, age, **kwargs)
        elif animal_type == 'Cat':
            return Cat(name, age, **kwargs)
        elif animal_type == 'Fish':
            return Fish(name, age, **kwargs)
        elif animal_type == 'Humster':
            return Humster(name, age, **kwargs)
        else:
            raise ValueError(f'Error animal type {animal_type}')


spanky = AnimalFactory.create_animal('Dog', 'Спанки', 3, breed='Йоркшер')
tom = AnimalFactory.create_animal('Cat', 'Том', 15, color='Blue')
dorry = AnimalFactory.create_animal('Fish', 'Дорри', 4, habitat='Дом')
polly = AnimalFactory.create_animal('Humster', 'Полли', 1, fur_color='Коричневый')
rory = AnimalFactory.create_animal('Fish', 'Рори', 9, habitat='В зоопарке')
nor = AnimalFactory.create_animal('Humster', 'Норри', 2, fur_color='Золотой')
# pampidy = AnimalFactory.create_animal('Morkov', 'Пампиду', 3, habitat='На улице')

for animal in [spanky, tom, dorry, polly, rory, nor]:
    print(animal.get_special())
