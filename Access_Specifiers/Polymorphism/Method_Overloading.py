# Method overloading is compile time polymorphism


# here i just used 2 parameters and assign 2 values
class Substraction:
    def sub(self,a,b):
        self.a = a
        self.b = b
        return self.a - self.b

object_1 = Substraction()
print(object_1.sub(13,9))

#==========================#
# here i took 3 parameters and assign 3 values but through an error bcoz when i run this code it will consider the second def
class Substraction:
    def sub(self,a,b):
        self.a = a
        self.b = b
        return self.a - self.b
        
    def sub(self,a,b,c):   #when we run the code it will through the error bcoz python will consider the latest the latest parameters
        return a-b-c

object_1 = Substraction()
print(object_1.sub(13,9))
print(object_1.sub(13,11,4))


#============================#

# but we can achive the above error using the " default argument "


class Substraction:
    def sub(self,a,b,c = 1):
       
        return a - b - c
        
object_1 = Substraction()
print(object_1.sub(13,9))
print(object_1.sub(13,9,5))


#====================#

# Using " args"

class Substraction:
    def sub(self,*args):
        n = 0
        for iter in args:
            n -= iter
        return n
        
object_1 = Substraction()
print(object_1.sub(13,9))
print(object_1.sub(13,9,5))
print(object_1.sub(13,9,8,6,5))





