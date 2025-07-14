student1 = {'name':"Veer", 'age':10}
student1['age']=20
if student1['age']<13:
    print("Student is Kid")
elif student1['age']>20:
    print("Student is adult")
else:
    print("Student is teenager")
# = is used for assigning the value
# == is used for checking if the value matches or not

#practice_example 1 : set the temprature
temprature=25
if temprature>20:
    print("Hot!")
else:
    print("Cold!")

#practice For loop
colors = ["red", "yellow", "blue"]
for color in colors:
    print(color)

for number in range(5):
    print(number)
"""
range() makes a sequence of numbers
range(3) will make squence from 0,1,2
range(1,4) will make sequence from 1,2,3
"""

animals = ["tiger"]
for animal in animals:
    print(animal)


#practicing the while loop
number=0
while number<=5:
    print(number)
    number=number+number+1


#practicing while loop again
number = 10
while number>1:
    number = number-1
    print(number)


#Checking if the number is even or odd
numbers = [1,2,5,6,7,9]
for number in numbers:
    if number%2==0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

#example to check positive or negative
numbers = [1,2,-3,5,6,-9]
for number in numbers:
    if number > 0:
        print(f"{number} is positive")
    else:
        print(f"{number} is negative")

#example to use break and continue
for number in numbers:
    if number == 2:
        continue #using continue will skip the turn
    elif number == 6:
        break #using break will exit the loop
    else:
        print(number)
"""
Testing exact boundaries and empty lists is a best practice
"""
    
#weatehrchecker app
weather ="rain"
if weather=="rain":
    print("Take unbrella with you!")
else:
    print("Have a great sunny day!")

#print numbers 10 to 15
for count in range(10,16):
    print(count)


#count backwards from 5 to 1, using while loop
count = 5
while count>=1:
    print(count)
    count=count-1
    
#add multiple of 3
for count in range(1,11):
    print(count)
    if count%3==0:
        print("Multiple of 3")