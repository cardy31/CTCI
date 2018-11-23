from enum import Enum


def main():
    shelter = AnimalShelter()
    shelter.enqueue(AnimalType.DOG)
    shelter.enqueue(AnimalType.CAT)
    shelter.enqueue(AnimalType.DOG)
    shelter.enqueue(AnimalType.DOG)
    shelter.enqueue(AnimalType.CAT)
    shelter.enqueue(AnimalType.CAT)

    print(shelter)

    print(shelter.dequeue_cat())
    print(shelter.dequeue_dog())

    print(shelter)

    print(shelter.dequeue_any())

    print(shelter)


class AnimalShelter:
    def __init__(self):
        self.__dogs = []
        self.__cats = []
        self.__age = 0
        self.__oldest_animal = AnimalType.DOG

    # Dequeue the oldest animal
    def dequeue_any(self):
        # No dogs, but still cats
        if not self.__dogs and self.__cats:
            return self.__cats.pop()
        # No cats, but still dogs
        elif not self.__cats and self.__dogs:
            return self.__dogs.pop()
        # No animals at all
        elif not self.__cats and not self.__dogs:
            return None

        # Dogs and Cats
        if (self.__dogs and self.__cats) and self.__dogs[-1].age < self.__cats[-1].age:
            return self.__dogs.pop()
        else:
            return self.__cats.pop()

    def dequeue_cat(self):
        if self.__cats:
            return self.__cats.pop()
        return None

    def dequeue_dog(self):
        if self.__dogs:
            return self.__dogs.pop()
        return None

    def enqueue(self, animal_type):
        if isinstance(animal_type, AnimalType):
            if animal_type == AnimalType.DOG:
                self.__dogs.append(Animal(animal_type, self.__age))
            elif animal_type == AnimalType.CAT:
                self.__cats.append(Animal(animal_type, self.__age))
            self.__age += 1

    def __str__(self):
        dog_str = ''
        for dog in self.__dogs:
            dog_str += dog.__str__()
            dog_str += ', '

        cat_str = ''
        for cat in self.__cats:
            cat_str += cat.__str__()
            cat_str += ', '
        return 'Dogs: [{}]\nCats: [{}]'.format(dog_str, cat_str)


class Animal:
    def __init__(self, animal_type, age):
        if isinstance(animal_type, AnimalType):
            self.type = animal_type
        self.age = age

    def __str__(self):
        return 'Age: {}, Type: {}'.format(self.age, self.type.name)


class AnimalType(Enum):
    DOG = 1
    CAT = 2


if __name__ == '__main__':
    main()
