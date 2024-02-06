
#========EX:1==============
class ComplexNumber:
    def __init__(self,real,imaginary):
        self.a = real
        self.b = imaginary
        
    def __add__(self,other):
        return f"{self.a + self.b} + {other.a + other.b}i"

object_1 = ComplexNumber(1,2)
object_2 = ComplexNumber(3,4)
print(object_1 + object_2)

#========EX:2==============
class CustomString:
    def __init__(self,preffix,saffix):
        self.a = preffix
        self.b = saffix
        
    def __add__(self,other):
        c = self.a
        d = self.b + other.b
        return CustomString(c,d)
    
    def __str__(self):
        return (self.a + self.b)

object_1 = CustomString("Prefix: ", "Hello")
object_2 = CustomString("Prefix: ", "World")
print(object_1 + object_2)
  # Output: Prefix: HelloWorld
  
 #========EX:3==============
class Child:
    def __init__(self,name,height):
        self.a = name
        self.b = height
        
    def __gt__(self,other):
        if (self.b > other.b):
            return True
        else:
            return False
        
object_1 = Child("Nischay", 8)
object_2 = Child("Nyna", 5)

if object_1>object_2:
    print(f"{object_1.name} will allow")
else:
    print(f"{object_2.name} will allow")

  
  
  
  
