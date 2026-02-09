class company():
    def __init__(self):
        self.__companyname="google"
    #def companyname(self):
       #print(self.__companyname)

a=company()
a.companyname()

#example private
class bank():
    def __init__(self):
        self.__balance=0
    def showbalance(self):
        print("your bank balance:",self.__balance)
    def deposit(self):
        amount=int(input("Enter deposit amount:"))
        self.__balance+=amount
        print("amount deposited successfully")
    
a=bank()
a.showbalance()
a.deposit()
a.showbalance()
#example protected
class Parent:
    def __init__(self):
        self._data = "Hello"
class Child(Parent):
    def show(self):
        print(self._data)

c = Child()
c.show()


