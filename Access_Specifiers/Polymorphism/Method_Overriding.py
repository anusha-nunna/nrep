# Method overriding is run time polymorphism
# it occurs in two clasess. it will occur in inheritance
# method name same and parameters are same

class Class:
    def uniform(self):
        print("every student should ware the collage uniform")
    def color(self):
        print("different branch ishaving different color")
object_1 = Class()
object_1.uniform()

#===============================#
# method overriding will occur at run time. when we call method name it will print child class print definition
class Class:      # parent class
    def uniform(self):
        print("every student should ware the collage uniform")
    def color(self):
        print("different branch is having different color")
        
class Branch(Class):     #sub class
    def color(self):
        print("one color is mandatory for every branch")   #defining own definition
        
object_1 = Branch()    #using child class
object_1.color()     # calling child method

