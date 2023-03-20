- class method is defined for a class. @classmethod decorator is used to convert a method to class method
- parameter passed to class method is cls (representing class/class object is passed as first argument)
- class methods are used when need to access class variables and perform some operation without using object
- To call class method, you can use <classname>.<instancename> or <objname>.<instancename>

- static method are regular functions that can receive regular parameters so dont need to send class/object as first argument
- These methods don't touch any class / object attributes so we dont have self or cls here
- To call static method, you can use <classname>.<instancename> or <objname>.<instancename>
- We use them as normal functions but static methods allows to organize them in class. 
- Ex. Class Math with static functions for each math operation -> allows us to organize code -> import module and call function using math.<fnname> ; not instantiate static method but required for normal class method.
 
    class Math:
        @staticmethod
        def add(x,x2):
            return x+x2

    Call above method using -> Math.add()