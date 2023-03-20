"""
Class overriding methods -> override standard methods on custom class ex. +,-,*,/    
    
"""

import math 

class Point():
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        self.coords = (self.x, self.y)
        
    def move(self,x,y):
        self.x+=x
        self.y+=y
        
    def __str__(self):
        return "(" + str(self.x) + ',' + str(self.y) + ')'
    
    def __len__(self):
        return int(math.sqrt(self.x**2 + self.y**2))
        
    def __add__(self,p):   #Use default methods called magic methods
        return Point(self.x+p.x,self.y+p.y)
    
    def __sub__(self,p):   #Use default methods called magic methods
        return Point(self.x-p.x,self.y-p.y)
    
    def __mul__(self,p):   #Use default methods called magic methods
        return (self.x*p.x) + (self.y*p.y)
    
    def __gt__(self,p):
        return len(self) > len(p)
        
    def __ge__(self,p):
        return len(self) >= len(p)
        
    def __lt__(self,p):
        return len(self) < len(p)
        
    def __le__(self,p):
        return len(self) <= len(p)
        
    def __eq__(self,p):
        return (self.x==self.x) and (self.y==p.y)
        
        
p1=Point(3,4)
p2=Point(3,2)
p3=Point(1,3)
p4=Point(0,1)

p5=p1+p4
print(p5)

num=p2*p3
print(num)

print(len(p1))
print(p1>p2)
print(p2==p3)
print(p4<=p1)