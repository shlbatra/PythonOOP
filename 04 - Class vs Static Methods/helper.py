# When to use class methods and when to use static methods ?


class Item:
    @staticmethod
    def is_integer(num):#regular parameter
        '''
        This should do something that has a relationship
        with the class, but not something that must be unique
        per instance!
        Similar to normal function with parameter related to class
        '''
    @classmethod
    def instantiate_from_something(cls):#mandatory parameter
        '''
        This should also do something that has a relationship
        with the class, but usually, those are used to
        manipulate different structures of data to instantiate
        objects, like we have done with CSV.
        '''

# THE ONLY DIFFERENCE BETWEEN THOSE:
# Static methods are not passing the object reference as the first argument in the background!


# NOTE: However, those could be also called from instances.

item1 = Item()
item1.is_integer()
item1.instantiate_from_something()