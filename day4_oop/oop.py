"""
- Class is a blu print for objects is uses CamelCase
- Each class attributes (variables) and methods (functions)
- use __init__ as a constructorm to set up and object when it it created
- use __del__ as deconstructor when object is destroyed
"""
class Book:
    def __init__(self, book_title:str, book_author:str):
        self.book_title = book_title
        self.book_author = book_author

my_book = Book("Curse of Minecraft", "Rushiraj")
print(my_book.book_author)

#example for inheritance
class Animal:
    def __init__(self, name):
        self.name=name

    def animal_sound(self):
        return "Some Sound"

class Dog(Animal):
    def animal_sound(self):
        return "Woof"

class Bird(Animal):
    def animal_sound(self):
        return "Cookoo"
    
animals = [Dog("Brian"), Bird("Choco")]
for animal in animals:
    print(animal.name,animal.animal_sound())


#example with Banks for polymorphism
class BankAccount:
    def __init__(self, balance):
        self.__balance=balance

    def deposit(self,amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance
    
account = BankAccount(100)
account.deposit(59)
print(account.get_balance())

"""
You can still access the pricate keywords because of name mangling but it is commen knowledge and a sign for other developers,
That this code should be treated as private and must not be accessed.
"""
#example with Cars
class Cars:
    def __init__(self,vehicle_id:str):
        self._vehicle_id=vehicle_id

    @property
    def vehicle_id(self):
        return self._vehicle_id
    
my_car=Cars("22RIP")
print(my_car.vehicle_id)

