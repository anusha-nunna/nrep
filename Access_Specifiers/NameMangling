# NAME MANGLING 2 ways
#1st way
class Class:
    def __init__(self):
        self.name = "anusha"
        
    def display(self):
        self.__age = 24    # age is private
    
object_1 = Class()

object_1.display()
print(object_1._Class__age)

#===============================================================
# 2nd way
class Class:
    def __init__(self):
        self.name = "anusha"
        
    def __display(self):
        self.__age = 24    # age is private
        
    def DisplayPrivateData(self):
        self.__display()
        
object_1 = Class()

object_1.DisplayPrivateData()
print(object_1._Class__age)
