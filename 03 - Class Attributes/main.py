class Item:
    #attribute global across all instances - class attributes
    pay_rate = 0.8 # The pay rate after 20% discount  #class attribute
    all = [] #class attribute 
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        #instance attributes
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute , add each time to all when instance is created
        Item.all.append(self)  #class attribute referenced here

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate  #or Item.pay_rate, class attribute can be referenced via self - object or cls - class

    def __repr__(self):
        #representing your object with print command 
        # another method similar called __str__
        return f"Item('{self.name}', {self.price}, {self.quantity})"

item1 = Item("Phone", 100, 1)  
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

#Access all items in our shop rt now - list with 5 elements - each element instance of class
# class attribute used for this purpose is all 
print(Item.all)  # list with 5 instances with their memory address
#To change way object represented with print, use magic method called __repr__

for instance in Item.all:
    print(instance.name)



#Item after discount
item1.apply_discount()
print(item1.price)

#Item after custom discount 
item2.pay_rate = 0.7 
item2.apply_discount()  # If use Item.pay_rate in apply_discount then always use class level attribute 
print(item2.price)


# Magic attribute to see all attributes belong to object
print(Item.__dict__) #class level attributes - payrate 
print(item2.__dict__) #object level attributes - name, price and quantity

#class level reference
#from class
#print(Item.pay_rate)
#from instance level - get from instance level first then class level second
#print(item1.pay_rate)