#abstraction
#@abstractmethod-decorator 
from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass 
class bike(vehicle):
    def start(self):
        print("bike start")
class car(vehicle):
    def start(self):
        print("car start")
    
a1=car()
a1.start()

a2=bike()
a2.start()

#example 
from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod       
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
    @abstractmethod
    def balance(self):
        pass
class SBI(Bank):
    def deposit(self):
        print("Deposit amount in SBI")
    def withdraw(self):
        print("Withdraw amount from SBI")
    def balance(self):
        print("SBI balance is 10,000")

s = SBI()
s.deposit()
s.withdraw()
s.balance()

        
        