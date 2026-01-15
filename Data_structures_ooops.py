class Animal:
    #first thing inside class is Constructor
    def __init__(self,num_of_legs, body_type, tail):
        self.num_of_legs = num_of_legs
        self.body_type = body_type
        self.tail = tail
        
    
#methods-functions created inside class

#Getter methods 
def get_Legs(self):
    print ("The number of legs are: ", self.num_of_legs)
    
#setter methods
def set_body_type(self, body_type):
    self.body_type = body_type
    
#custom method     
def speak(self):
    print("Animal Speaks")
#Obeject
dog = Animal(4, "rough", "Yes")


print(dog.num_of_legs)
print(dog.body_type)
print(dog.tail)


#Inheritance

class Animal:
    def eat():
        print("Animal is eating ")
    def sleep():
        print("Animal is sleeping")

#Chld Class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
        
#Object
d=Dog()
d.eat()
