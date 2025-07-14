"""
Always add comments on the top of the function to explain what it does really
"""
def greet(name):
    print(f"Good Morning!, {name}")

"""
Functions are made for doin one thing, Don't cram too much init
"""
greet("Aarush")
greet("Jay")

#example 2 for adding two numbers
def add_numbers(number1=0, number2=0):
    sum = number1 + number2
    print(f"Sum of {number1} and {number2} is {sum}")

add_numbers(3,4)

#function to multiply the number
def multiply_numbers(num1=0,num2=0):
    multiplication_result=num1*num2
    print(f"{num1}x{num2} {multiplication_result}")

multiply_numbers(num2=10, num1=11)

#function that returns values
def get_name(name="Jai"):
    if name=="Jai":
        return "Flame"
    else:
        return name

print(get_name("Jai"))

#function to square the number
def square_num(num=0):
    square = num*num
    return square

square_num = square_num(20)
print(square_num)
    
"""
Avoid using global variables but global variables live in full code
To use global variable inside the function use global keyword
"""
count = 0
def increment():
    global count
    count += 1

increment()
print(count)

"""
Each function should do one thing, like calculate area, not calculate and print the area
"""

#function to check if number is even or not
number = 11

def isEven(num:int)->bool:
    if(num%2==0):
        return True
    return False #skipping the else statement line here, because only reason code will reach here will be when if condition is false

def print_isEven(num:int):
    if(isEven(num)):
        print(f"{num} is Even")
    else:
        print(f"{num} is not Even")

print_isEven(number)

#This function is to print the list 
def print_item_list(list:list):
    for item in list:
        print(item)

item_list=["Cake", "Bun", "Cookies"]
print_item_list(item_list)