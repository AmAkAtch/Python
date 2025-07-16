#Example1: Reading file
"""
Open any file using open("file path unless in same folder", "operation")
r - read
w - write
a - append
"""
file = open("test.txt","r")
content=file.read()
print(content)
file.close() #closing file is important otherwise it stays open in memory


#Example2: Better way to read file using with
with open("test.txt","r") as file:
    content=file.read()
    print(content)
"""
Using with eliminates the need to close the file to release it from the memory
"""


#Example3: Read line by line
with open("test.txt","r") as file:
    line1 = file.readline().strip()
    line2 = file.readline().strip() #using strip removes "\n" and empty spaces from the start and end of the Line
    print(line1,line2)


#Example4: using For loop
with open("test.txt", "r") as file:
    for line in file:
        print(line.strip())


#Example5: Reading the lines and adding them in list
with open ("test.txt", "r") as file:
    lines = file.readlines()
    print(lines)


#Example6: Writing Lines to the file
with open("test.txt","w") as file: #When file doesn't exsit it will create a new file
    file.write("Hellow This is new text!\n") #Writing this multiple times make 
    file.write("Hellow this is second new Line")


#Example7: When you don't want to rewrite the file but want to add to the file
with open("test.txt","a") as file:
    file.write("\nHellw this is extra line added later")
