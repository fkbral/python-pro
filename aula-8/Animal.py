class Animal:
    def __init__(self, name, region, population):
        self.name = name
        self.region = region
        self.population = population
        self.endangered = False

    def __add__(self, other):
        return self.population + other.population

    def __sub__(self, other):
        return self.population - other.population

    def __gt__(self, other):
        return self.population > other.population

    def __ge__(self, other):
        return self.population >= other.population

    def __lt__(self, other):
        return self.population < other.population

    def __le__(self, other):
        return self.population <= other.population

    def __eq__(self, other):
        return self.population == other.population

    def __ne__(self, other):
        return self.population != other.population

    def reproduce(self, descendents=0):
        if self.name == "rabbit":
            self.population += 10
            return

        if self.name == "dog":
            self.population += 5
            return

        if self.name == "giraffe":
            self.population += 1
            return

        self.population += descendents
        return


dogs = Animal('dog', 'all', 1e8)
cats = Animal('cat', 'all', 1e9)

print(cats - dogs)
print(dogs.__add__(cats))

print(f'As populações são iguais?{dogs == cats}')

# Tanto faz como chamo meu método reproduce
# Posso chamá-lo pela classe
# Animal.reproduce(dog)
# Como pelo objeto criado:
# dog.reproduce(100)

dogs.reproduce()
cats.reproduce(2)

print(dogs.population)
print(cats.population)
