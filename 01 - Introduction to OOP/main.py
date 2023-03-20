# How to create a class:
class Item:
    def calculate_total_price(self, x, y):  #Function inside class called method
        return x * y

# How to create an instance of a class
item1 = Item()
#random_str=str("4")
#random_str.upper()  #Method for in built class to execute on instance

# Assign attributes to instances:
item1.name = "Phone"
item1.price = 100
item1.quantity = 5

# Calling methods from instances of a class:
print(item1.calculate_total_price(item1.price, item1.quantity))

# How to create an instance of a class (We could create as many as instances we'd like to)
item2 = Item()

# Assign attributes
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3

# Calling methods from instances of a class: 
print(item2.calculate_total_price(item2.price, item2.quantity))