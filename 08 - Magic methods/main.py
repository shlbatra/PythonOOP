'''
a=1
print(str(a) + '11')
'''

class CustomizedInteger:
    def __init__(self, integer):
        self.integer=integer

    #def __str__(self):
    #    return f'Customized Integer {self.integer}'

    def __str__(self):
        if self.integer == 4:
            return 'Four'
            
    def __repr__(self):
        return f'CustomizedInteger({self.integer})'



int1 = CustomizedInteger(4)
print(str(int1))  
print(int1)
#get memory object as dont do anything without __str__ method yet in class
#by default, print convert to str

# print built in function show object using __str__ first if not then look in __repr__ 
# __repr__ is unambigous method -> return valid python code that allows us to recreate the object that we just created. Return exactly as the object is created.



