class Dog:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age

mikey = Dog("Mikey", 6)
philo = Dog("Philo", 5)

mikey.age = 7
philo.name = ("Nana")

print("{} is {} and {} is {}".format(philo.name, philo.age, mikey.name, mikey.age))