#functions can be represented as objects 

def f1():
    print("Called f1")
    
def f2(f):
    f()

f1()

print(f1) # f1 is an object so pass around a program

f2(f1) #pass f1 object as a paramete of f2 

#Wrapper Function 
print("\n\nWrapper Function")
def f1(func):
    def wrapper():
        print("Started")
        func()
        print("Ended")
    
    return wrapper #return function defined inside it. 

def f():
    print("Hello")
    
f1(f)  # nothing happened as just return function and not call the function 
print(f1(f)) #function returned at the memory address
f1(f)() #here the returned function is called


#Decorate function - Everytime call f then  do functionality of f2 
print("\n\nDecorate Function")
x=f1(f)   # set f variable - function f1 with parameter f , function aliasing - changing name of function and functionality 
x()

#Replace line 35 with decorator 
print("\n\nDecorators")

@f1
def f():
    print("Hello")
    
#decorate f with f1 function,basically pass f function to f1
f()

#decorator with parameters - use args and kwargs in this scenario
print("\n\nDecorators with parameters")

def f1(func):
    def wrapper(*args, **kwargs):  #this function has some number of arguments, no idea what it would be
        print("Started")
        func(*args, **kwargs)
        print("Ended")
    return wrapper

@f1
def f(a):
    print(a)
    
f("Hi!")

#returning values from decorated functions
print("\n\nReturning values from decorated functions")

def f1(func):
    def wrapper(*args, **kwargs):  #this function has some number of arguments, no idea what it would be
        print("Started")
        val=func(*args, **kwargs)
        print("Ended")
        return val
    return wrapper

@f1
def add(x,y):
    return x+y

print(add(9,6))


























