#loop run until condition false
#print number  1to5 using while loop
i=1
while(i<6):
    print(i)
    i=i+1
#write loop statement to print following series 10to200
i=10
while(i<=200):
    print(i,end=",")
    i=i+10

#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop
fruits=['banana','orange','mango','lemon']
fruits.append('lemon')
i=len(fruits)-1
while i>=0:
    print(fruits[i])
    i-=1
