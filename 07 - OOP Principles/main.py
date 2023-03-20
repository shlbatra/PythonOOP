from phone import Phone
from keyboard import Keyboard
from item import Item


'''
item1=Item("MyItem",750)
item1.apply_increment(0.2)  #Encapsulation, not direct access to price, modify attribute by method
item1.apply_discount()

item1.send_email() -> send email about this item, connect to smtp 
server and body of email with message, need lot of new methods before 
send email 
'''

'''
item2=Item("MyItem",750)
item1=Phone("jscPhone",1000,3)

item1.send_email()   #item1 inherits item method from phone child class
item2.send_email()

In above 2 lines, also implement Polymorphism -> one single entity 
that you can use for multiple objects. 
So, we think of inheritance and polymorphism combined. 

'''

item1 = Keyboard("jscKeyboard", 1000, 3)
item1.apply_discount() #use single entity from diff kind of objects for item, phone and keyboard class 
# control disc amt in classes using class attribute 


print(item1.price)

item2 = Item("jscKeyboard", 1000, 3)
#item2.__connect -> private methods still can be accessed by object but as good practice, these are marked as hidden and programmers should not access these methods 

