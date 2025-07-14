x = 10
y = 3
print(x*y, x-y, x+y, round(x/y, 2))


word="fun"
print((word + " ")*5)

foods = ["pizza", "sushi"]
foods.append("tacos")
foods.remove("sushi")
print(foods)

"""
Make sure that the values inside the dictionary are assigned to key via :
Also make sure that while accessing the specific key of dictionary you have to use []
"""
profile = {'name':"sam", "age":30}
profile["job"]="coder"
profile["age"]=31
print(profile)