#use to instantiate instances - create data that will represent something

from item import Item
from phone import Phone 

# Call class method
#Item.instantiate_from_csv()
#print(Item.all)

item1 = Item("MyItem", 750)
# Setting an Attribute - override the name
item1.name = "OtherItem" #if attribute defined as read only using @property then need @name.setter to allow for this to work

#If restrict behaviour for name change after set up in initialization
#create read only attributes - set only at one time - initilization and error if override - encapsulation

#call property - name 
print(item1.name)

#error out below =
#item1.read_only_name = "BBB"
#item1.name = "OtherItem" 

#set attribute value after setter -> call name.setter with parameter
#item1.name = "Other Property"

# Getting an Attribute -> call name(self) function 
#print(item1.name)

