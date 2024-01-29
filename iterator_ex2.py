class Sentence:
    def __init__(self,sentence):
        self.a = sentence
        self.index = 0  #keep track of the current position while iterating over the words
        self.b = self.a.split()  #Splits the input sentence into words
    def __iter__(self):   #make the class iterable
        return self
        
    def __next__(self):   #generating the next item
        if self.index >= len(self.b):
            raise StopIteration
        var = self.index
        self.index += 1
        return self.b[var]

object = Sentence("Hello Anusha How are you")
for iter in object:
    print(iter)
    
