class Dog:
    Species = "Chiwawa"
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    def show_dog(self):
        print("name:",self.name, "Age:", self.age, "Breed:", self.breed)
    def Show_sound(self, sound):
        print("Sound: ",sound)
    @classmethod
    def Show_species(cls):
        print("Species: ",cls.Species)
    @staticmethod
    def Height_dog(height):
        if height > 80:
            return "Big Dog"
        elif 50 < height < 80:
            return "Standard Dog"
        else:
            return "Small Dog"

dog = Dog("jammy", "5", "chiwawa")
dog.show_dog()
dog.Show_sound("hong hong hong")
dog.Show_species()
print(dog.Height_dog(20))