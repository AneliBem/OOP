class Dog:
    def __init__(self, name, age):
       self.name = name
       self.age = age

    def __sit(self):
        return my_dog.name + " is now sitting."

    def _sit(self):
        return my_dog.name + " is now sitting."
    
    def sit(self):
        return my_dog.name + " is now sitting."


my_dog = Dog("John", 10)    

print(my_dog.name)

# Encapsulation
print(my_dog._Dog__sit())
print(my_dog._sit())
print(my_dog.sit())