#hello world program
print("Hello world")

#Variable task 1
age = 20           #num
name = "Abi"       #text
print(age)
print(name)

#Data Types int

age = int(input("Enter your age: "))   
print("Your age is:", age)
 #float

heat = float(input("Enter the temperature: "))  # Convert input to float
print("The temperature is:", heat)
#String

city = input("Enter your city: ")
print(city)
#boolean

student = input("Are you a student? yes/no: ").strip().lower()  
if student == "yes":
 print(True)
else:
 print(False)