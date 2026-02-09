#task area of rectangle 
class shape():
    def area(self):
        return 0
class rectangle(shape):
    def area(self):
        l=10
        b=20
        print(l*b)

a=rectangle()
a.area()

#task 
class person():
    def __init__(self,name):
        self.name=name
class student(person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade
    def display(self):
        print("name:",self.name,"grade:",self.grade)
        
a=student("abi","a") 
a.display()

#task
class vehicle():
    def start(self):
        print("vehicle started")
class car(vehicle):
    def start(self):
        print("car started")

a=car()
a.start()

#task
class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
class manager(employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def display(self):
        print(self.name,self.salary,self.department)

a=manager("abi","50000","Developer")    
a.display()   
        