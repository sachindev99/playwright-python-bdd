class Parent:
    def greet_from_parent(self):
        return "Hello from Parent"


class Child(Parent):
    def greet_from_child(self):

        return "Hello from Child"


c=Child()
c.greet_from_parent()

#------------------------------------------

class Parent:
    x = 100
    def greet_from_parent(self):
        return "Hello from Parent"


class Child(Parent):
    
    def greet_from_child(self):
        print(super().greet_from_parent())#to access the parent class method we use super keyword
        print(super().x)
        return "Hello from Child"


c=Child()
c.greet_from_child()

add = lambda a,b:a+b
print(add(10,20))

numbers = [1,2,3,4,5]

square_numbers = map(lambda i:i*2,numbers)
print(list(square_numbers))


