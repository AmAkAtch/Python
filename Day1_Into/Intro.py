#Example 1 - Syntax and comments
print ("Hello, World !")
if True:
    print ("This is indented block !")
    #Indetation is exactly 4 blocks
"""
Adding commentst that explain code better
is very necessary as the best practice
"""

#Example 2 - Good practice 
print ("This is")
print ("Good practice")
#You can put multiple lines in on-line with the help of ;
print ("This is"); print("Bad practice")

#Exmaple 3 - Variables
name = "Rushiraj"
Name = "Veer"
veer_age =  10 #standard in python is to snake_case. 
print(Name)
"""Python is case sensitive!"""

#Example 4 - operations
earned_money = 30
robbed_money = 20
total_money = earned_money+robbed_money
shared_cut = total_money/2 #after devision python returns float
print(total_money)
print(f"2 People's cut in totla money = {shared_cut}")
temp = 24.567
print(round(temp, 2)) 
"""
While printing the float you can round of upto certain decimals
This will not change the original value
To get rounded value, store it inside new variable
"""
print(temp)

#example 5 - Strings
first_name = "Rushiraj"
last_name = 'Gadhavi' #You can use either "" or '' for declaration of the string
print(first_name+" "+last_name)
print("ha"*3) # using * will repeat the string 

#example 6 - Lists
shopping_list = ["bread", "butter", "jam"]
print(shopping_list)
print(shopping_list[1]) #how to access the specific item from the array
"""
Add or remove items from the list using append or remove
"""
shopping_list.append("cheez")
print(shopping_list)
shopping_list.remove("butter") 
print(shopping_list)

#example 7 - Dictionaries
student1 = {"name":"Veer", "age":10} #store multiple things abou one single person or something as key value pairs
print(student1)
print(student1["name"]) #access specific value with the help of key of any perticular dictionary
student1["city"]="Anand" #add more key-value pairs on the fly
print(student1)
student1['age']=15 #update the existing the eky-value pair
print(student1)

#example 8 - final homework practice
my_name = 'Rushiraj'
age = 25
print(f"My name is {my_name} and I am {age} years old")

#Best Practices
"""
Clearly name your variables because your team needs to understand
Add notes to explain the tricky part
always 4 spaces for the indentation
One idea per line and break the code sections with multiple blank space
Test small pieces of code before aligning them
"""