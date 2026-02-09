#same method name, different behavior
class animal():
    def sound(self):
        print("animals makes sound")

class dog(animal):
    def sound(self):
        print("dog barks")

class bird(animal):
    def sound(self):
       print("birds sing")

a=animal()
a.sound()