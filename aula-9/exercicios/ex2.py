class Person:
    persons = []

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        Person.persons.append(self)

    @staticmethod
    def printAgeStatistics():
        ages = []
        for person in Person.persons:
            ages.append(person.age)

        newest = min(ages)
        oldest = max(ages)
        average = sum(ages)/len(ages)

        print(f'A pessoa mais nova tem {newest}')
        print(f'A pessoa mais velha tem {oldest}')
        print(f'A média das idades é {average}')


john = Person('John', 22, 80.5)
mary = Person('Mary', 28, 62)

Person.printAgeStatistics()
