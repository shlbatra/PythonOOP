"""
Important and used when coding fairly large projects with multiple classes    
"""

class Dog:
    dogs=[] #class variable , variable every object of your class might need statically 
    
    def __init__(self,name):
        self.name=name 
        self.dogs.append(self) #append dog object to list dogs ie class attribute
        
    @classmethod #decorators -> modify behaviour of method
    #call it on name of class, argument passed is name of class
    #access class variables without using object
    def num_dogs(cls):
        #use class arguments / static methods / other methods in class
        return len(cls.dogs)
    
    @staticmethod
    def bark(n):
    #dont need class / object as argument, only pass arguments we need similar to regular function
    #dont touch any class / object attributes as we dont have self or cls here
    #use them as a function but organize them in class. 
    #ex. class Math with static functions for each math operation -> allows us to organize code -> import module and call function using math.<fnname> 
        """
        bark n times
        """
        for _ in range(n):
            print("Bark!")
            
tim = Dog("tim")
jim = Dog("jim")
print(Dog.dogs) #class name can be used to call class method or with object name as well
print(tim.dogs)

print(Dog.num_dogs()) #call class method on class itself , also call it on object as well 
print(tim.num_dogs()) #generally not good practice as call using class name 

Dog.bark(10) #call static method directly from class as well or object too


