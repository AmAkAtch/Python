try:
    number = int(input("Enter the number: "))
    result = number/0
except ValueError:
    print("Enter proper number please")
except ZeroDivisionError:
    print("Can't divide by 0")

"""
You can use multiple except to catch different errors
"""

#example2: catching the specific error
try:
    with open("missing.txt","r") as file:
        file.read()
except FileNotFoundError:
    print("File doesn't exist")


#example3: using else and finally
try:
    number=int(input("Enter the number: "))
    result = number/10
except ValueError:
    print("Please enter the value in Numbers")  #this block catches the error
else:
    print(result)                               #This block will run if no error is caught
finally:
    print("Thanx for using our program")        #This block will run no matter the error or not


#example 4: raising the error
number = int(input("Enter the positive number: "))
if number<0:
    raise ValueError("Number should be greater than 0 to be positive")
print(number)