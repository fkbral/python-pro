class Animal:
    def __init__(self, name, region, population):
        self.name = name
        self.region = region
        self.population = population
        self.endangered = False

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

# Tanto faz como chamo meu método reproduce
# Posso chamá-lo pela classe
# Animal.reproduce(dog)
# Como pelo objeto criado:
# dog.reproduce(100)

dog.reproduce()
cats.reproduce(2)

print(dogs.population)
print(cats.population)
