import operator

print("Welcome to calculator Program")
print("""
 _____________________
|  _________________  |
| |              0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | ÷ | |
| |___|___|___| |___| |
|_____________________|
""")

def take_input():
    print("+")
    print("-")
    print("/")
    print('*')
    return input("Select the operator from above: ")

ops = {
    "+":operator.add,
    "-":operator.sub,
    "*":operator.mul,
    "/":operator.truediv
}

def calculate(first_num, op, second_num):
    return ops[op](first_num, second_num)

continue_calc = True
is_first_run = True

while continue_calc == True:
    if is_first_run:
        first_num = float(input("Enter the first Number: "))
        is_first_run = False
    else:
        first_num = result
    op = take_input()
    second_num = float(input("Enter the Second Number: "))

    result = calculate(first_num, op, second_num)

    print(f"{first_num} {op} {second_num} = {result}")

    userchoice = input("Do you want to start a new operation 'new' or continue on top 'cont'? or exit - 'exit': ")
    if userchoice == "new":
        is_first_run = True
    elif userchoice == "cont":
        is_first_run = False
    else:
        continue_calc=False

print("Thanks for using calculator")


