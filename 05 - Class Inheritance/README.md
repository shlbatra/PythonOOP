- Parent and Child classes 
- <child class>(<parentclass>)
- __init__ method for child class defined as -
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes / methods of parent class
        super().__init__(
            name, price, quantity
        ) #special arguments from parent class
- Child class extends functionality from parent class. ex. method to calculate not broken phones but cannot do in item as not have broken_phones attribute so create phone class - inherit functionality from item class