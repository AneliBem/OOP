class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "Some speak"
    
class Cat(Animal):

    def speak(self):
        return "Neow"

class Dog(Animal):

    def speak(self):
        return "Wof"
    
    def __sit(self):
        return my_dog.name.title() + " is now sitting."

    def _roll(self):
        return my_dog.name.title() + " is now roll."
    
    def sit(self):
        return my_dog.name.capitalize() + " is now stand up."


my_dog = Dog("john", 10)
my_cat = Cat("Bars", 5)    

# print(my_dog.name)

# Encapsulation
# print(my_dog._Dog__sit())
# print(my_dog._roll())
# print(my_dog.sit())

# Inheritance
print(my_cat.name, " speak to ", my_cat.speak())
print(my_dog.name.capitalize(), " speak to ", my_dog.speak())