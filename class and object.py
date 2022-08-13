
# Class is a blueprint or template of an object. It doesn't occupy memory space until object was created.

# for example string and List are inbuilt classes

# Creating a program code for a hotel to calculate bill for a customer.

class Anandhabhavan:   # classname


    def __init__(self, name, idly, vada, pongal, poori, dosa):    # __init__ is a default method in class
        self.name = name    # self is an argument used to hold the objects in class
        self.idly = 10 * idly
        self.vada = 8 * vada
        self.pongal = 40 * pongal
        self.poori = 30 * poori
        self.dosa = 25 * dosa


    def items(self):   # class method
        list = f'''customer Name : {self.name}\n Idly : {self.idly}.00rs\n Vada : {self.vada}.00rs
 Pongal : {self.pongal}.00rs\n Poori : {self.poori}.00rs\n Dosa : {self.dosa}.00rs\n'''
        return list

    
cust1 = Anandhabhavan('Anand', 2, 1, 1, 2, 1)   #object 1
cust2 = Anandhabhavan( 'Vignesh', 3, 2, 2, 2,2) #object 2


print(cust1.items())
print(cust2.items())

