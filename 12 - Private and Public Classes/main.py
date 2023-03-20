"""
Private class - used within same file or limited scope
Public class - access by everyone , any other class can access this class  
    
"""

class _Private:
    #Private class -> add _ before class name, everthing in class is private and dont want anyone to modify it 
    def __init__(self,name):
        self.name=name 
        
class NotPrivate:
    def __init__(self,name):
        self.name=name
        self.priv=_Private(name)
        
    def _display(self):
        #private attribute or method by adding _ in the start, tell other programmers not use it. They can still use it as Python doesnt stop it
        
        print("Hello")
        
    def display(self):
        print("Hi")