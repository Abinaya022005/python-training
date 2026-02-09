class goa:
    name=""
    def party(self):
        print("lets party....")
    def beach(self):
        print("enjoy in beach")
ramesh = goa()
ramesh.party()
suresh = goa()
suresh.beach()

ramesh.name="ramesh"
suresh.name="suresh"

print(ramesh.name)
print(suresh.name)

#task

class laptop:
    price=0
    processor=""
    ram=""
hp=laptop()
dell=laptop()

hp.price=50000
hp.ram="16gb"
hp.processor="i5"

dell.price=50000
dell.ram="16gb"
dell.processor="i5"

print(hp.price)
print(dell.price)

#task
class student:
    def __int__(self):
        self.name="abinya"
        self.regno="12345"
    def display(self):
        print("name:",self.name)
        print("reg no:",self.regno)

s1=student()
s2=student()

s1.name="abinaya"
s1.regno="1"

s2.name="anu"
s2.regno="2"

s1.display()
s2.display()

#task use parameter
class fruit:
    def __init__(self,col):
        self.color=col
apple=fruit("red")
print(apple.color)

#task
class calculator:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def add(self):
        print("add:",self.num1+self.num2)
    def sub(self):
        print("sub:",self.num1-self.num2)
    def mul(self):
        print("mul:",self.num1*self.num2)
    def div(self):
        print("div:",self.num1/self.num2)
a=int(input("enter a value a:"))
b=int(input("enter a value b:"))

obj1=calculator(a,b)

obj1.add()
obj1.sub()
obj1.mul()
obj1.div()



