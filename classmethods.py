#differnt types of class methods
#instance method
#class method
#static method
class laptop():
    chargertype = "C-TYPE"

    def __init__(self):
        self.brand=""
        self.price="24"
    def setprice(self,price):
        self.price=price
    def getprice(self):
        print(self.price)    
    @classmethod                  #decorator
    def changechargertype(cls):
        cls.chargertype="B-TYPE"
        print("charger type changed to B")
        

hp=laptop()
hp.setprice(24000)
hp.getprice()

laptop.changechargertype()