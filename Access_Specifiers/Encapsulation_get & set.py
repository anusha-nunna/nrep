#Encapulation Using get & Set method

class Car:
    def __init__(self,name,age):
        self.a = name
        self.__b = age

    def get_age(self):
        return self.__b
    def set_age(self,change):
        self.__b = change

object_1 = Car("Breeza", 4)
print(object_1.a)    #print the name
print(object_1.get_age())   #print the age

print("Here im using set method to change the previous value")
object_1.set_age(55)    #im trying set the value from 4 to 55
print(object_1.get_age())   #print the latest value
