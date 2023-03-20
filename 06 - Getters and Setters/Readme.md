- @property -> Property Decorator = Read-Only Attribute
Ex. 
@property
    def name(self):
        return self.__name
So, we cannot use self.name = name as read only. Need to use self.__name = name

- @<attributename>.setter to set value for attribute 
Ex. 
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value
 Once the setter method is defined, we can use item1.name = "OtherItem" to modify attribute value 

 - Create read only attributes that set only at initilization and error if override is encapsulation            
 - Encapsulation provides not direct access to attribute but modify attribute by method else error out if updated directly
