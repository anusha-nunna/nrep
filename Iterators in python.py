#coming to for loop when we create the list the values will be stored in memor but iter the values will not stored in the memory. when we use inbuild funtion "next" it will store the memory and print the value


#The only way to stop the exception for loop is that we need to raise StopIteration and it handles the exception internally 

#Using Iterator
class List:
    def __init__(self):
        self.num = 10
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= 20:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration
object = List()
for i in object:
    print(i)

# Using for loop
for i in range(1,11):
    print(i)

# given input and using for
list = [1,2,3,4,5]
for i in list:
    print(i)
 
# given input and using iter but it will only print single value everytime
list = [1,2,3,4,5]
object = iter(list)
print(next(object))
print(next(object))
