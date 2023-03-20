#Example with class

current_year=2022

class Person:
    def __init__(self, name, **kwargs):  #common use case in constructor class
        self.name=name
        self.yob=kwargs.get('yob')  #Returns None if not provided 
        
    def get_age(self):
        if self.yob:
            return current_year - self.yob
        
person1=Person(name="Sahil",yob=1988)
print(person1.get_age())

person1=Person(name="abc")
print(person1.get_age())
        