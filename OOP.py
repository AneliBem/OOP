class Dog:
    def __init__(self, name, age):
       self.name = name
       self.age = age

    def __sit(self):
        return my_dog.name.title() + " is now sitting."

    def _roll(self):
        return my_dog.name.title() + " is now roll."
    
    def sit(self):
        return my_dog.name.capitalize() + " is now stand up."


my_dog = Dog("john", 10)    

print(my_dog.name)

# Encapsulation
print(my_dog._Dog__sit())
print(my_dog._roll())
print(my_dog.sit())