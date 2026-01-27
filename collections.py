#list
#allow duplicate , any type store,we can modify

a=['apple','banana','mango','cherry','grapes']
a.append('cucumber') #added at the end
a.insert(0,'lime')   #0index added lime
a.pop(5)             #remove 5th position
print(len(a))        #length
a.reverse()          #reverse
print(a)
a.clear()             #clear
print(a)

# Tuple
#allow duplicate , any type store,cannot modify
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     
fruits = tuple(fruits)
print(fruits)    

#Set
#A set is a collection of unique items
fruits = {'banana', 'orange', 'mango', 'lemon','banana'}
fruits.add('berry')
print(fruits)

#Dictionary
#do not allow duplicate values,A dictionary is a collection of key-value pairs
a = {
    'name': 'Abinaya',
    'age': 20,
    'Location':'Salem',
    'grade': 'A'
}
a = {
    'name': 'Abinaya',
    'age': 20,
    'Location':'Salem',
    'grade': 'A'
}
a.update({'age': 21})
print(a.get('age'))
print(a)
