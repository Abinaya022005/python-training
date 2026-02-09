#variables
class phone():
    chargertype="C-TYPE"            #variable
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("brand:",self.brand)
        print("price:",self.price)
        print("chargertype:",self.chargertype)

samsung = phone("samsung","100000")
samsung.display()

moto=phone("moto","20000")
moto.display()