import csv
#Extend application and add more features
#Data and code are mantained seperate files - data in csv files
#Instantiate data from csv in a generic way

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod  #decorator to convert to class method (change behavior of function)
    def instantiate_from_csv(cls):
        # cant use self here -> this method to instantiate the object itself
        #  so this method not called from instance  -> convert to class method
        #cls parameter -> class object is passed as first argument 
        with open('04 - Class vs Static Methods/codesnippets/items.csv', 'r') as f:  
            reader = csv.DictReader(f)#read as list of dictionaries 
            items = list(reader) #convert to list 

        for item in items:
            #Instantiate our instances 
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            ) 
            #get list of dictionary

    @staticmethod
    def is_integer(num):
        #can receive regular parameter, not send instance as first argument
        #regular function that receives parameter
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float): #check received parameter instance of float 
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

#Call to class method
Item.instantiate_from_csv()
print(Item.all)    #-> store all instances of list 

#Call to static method- connection to class that we work with. ex. value is integer or not ?
print(Item.is_integer(10.0))

p1=Item('Laptop', 1000.0, 3)
p1.instantiate_from_csv()
print(p1)
print(p1.is_integer(10))


