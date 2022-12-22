# Dunder or Magic Methods

class Stock_details:
    
    def __init__(self, itemName, available_stock):
        self.itemName = itemName
        self.available_stock = available_stock

        
    #__add__ can perform addition operation in a class
    def __add__(self, other ):
        return self.available_stock + other.available_stock

      
    #  __ sub__ can perfom subtraction operation in a class 
    def __sub__(self, other):
        return f' {self.available_stock - other.available_stock} demand'
        
    # __len__ can find a length of the given string in a class
    def __len__(self):
        return len(self.itemName)
        
    # __getitem__ can perform slicing operation in a class
    def __getitem__(self, key):
        return self.itemName[key]
        
   # __contain__ to perform in operation in a class
    def __contain__(self, value):
        if value in self.itemName:
            return True
        else:
            return False
           
   # __eq__ can perform equal to  operation in a class
    def __eq__(self, other):
        if self.itemName == other.itemName:
            return True
        else:
            return False
           
block1 = Stock_details('Rice', 6750)
block2 = Stock_details('Wheat', 4380)
 
print(block1 + block2)
print(block1 -  block2)
print(block1 == block2)
print(len(block1))
print(block2[4])
print('e' in block1)