class a():
    def __init__(self):
        print("A")
    def display(self):
        print("you are in class a")
class b():
     def __init__(self):
        super().__init__()
        print("B")
     def display(self):
        print("you are in claa b")
class c(b,a):
     def __init__(self):
        super().__init__()
        print("C")
     def display(self):
        print("you are in claa c")

obj=a()
obj.display()
obj=b()
obj.display()
obj.display()