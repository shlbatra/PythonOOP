class Item:
    def __init__(self, name: str, price: float, quantity=0):#validate types here
        
        #declare in class what items to expect
        #Ex of Magic Method
        #can differentiate between mandatory and non mandatory items by passing default values 
        print(f"An instance created for : {name}")
        # Run validations to the received arguments
        #validate values here using assert statements
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object - dyanmic attribute assignment 
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
# You can add custom attributes as well
# item2.has_numpad = False 

print(item1.calculate_total_price())
print(item2.calculate_total_price())