#age eligiblity check
age=int(input("Enter your age:"))
if age >= 18:
    print("adult")
elif age>=13:
    print("teen")
else:
    print("child")

#operators
a=int(input("Enter a value a:"))
b=int(input("Enter a value b:"))
print(a,">",b,":", a > b)    
print(a, "==", b,":", a==b)   
print(a,"!=",b,":",a != b)   
print(a,"<=",b,a <= b)

#grade calculator
marks=int(input("Enter your mark:"))
if marks>=90:
    print("Grade A")
elif marks>=70:
    print("Grade B")
elif marks>=50:
    print("Grade C")
else:
    print("fail")