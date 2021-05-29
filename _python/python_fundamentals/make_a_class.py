class Dog:
    def __init__(self, name, breed, gender, size, age, potty_trained):
        self.name = name
        self.breed = breed
        self.gender = gender
        self.size = size
        self.age = age
        self.potty_trained = potty_trained
        self.is_good_dog = True
    
dog_one = Dog("Zoey", "Pitbull", "Female", "Big", 4, True)
dog_two = Dog("Spike", "English Bulldog", "Male", "Medium", True, .6)

print(dog_one.name)
print(dog_two.__dict__)