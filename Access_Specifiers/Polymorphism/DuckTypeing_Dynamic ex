#DUCK TYPYING: it focuses on the behaviour of objects rather than their types in duck typing we have 2 types Dynamic and Static
# 1).Dynamic: we no need to specify the type of the variable at compile time (python is a dynaic type
# 2).Static: we need to specify the type of the variable at compile time (C prog is static type)

# in dynamic class of the object doesn't matter method/attributes are matter. if the method is defined in the object then it will call

class Animal:
    def sound(self):
        print("animal can sound")
    def sleep(self):
        print("animal can slepp")

class Dog:
    def sound(self):
        print("dog can sound")
    def sleep(self):
        print("dog can sleep")
class Cat:
    def sound(self):
        print("cat can sound")
        
def display(self):   # self is a obj name
    self.sound()    #sound method is present in animal,Dog,Cat
    self.sleep()    #sleep method is present in animal,Dog
    
object_1 = Animal()
display(object_1)  #in animal sound & sleep method present so the o/p will displayed

object_2 = Cat()
display(object_2)   #show the error like 'Cat' object has no attribute 'sleep'. bcoz it not having the sleep method
