"""
1. Read numbers from a file called numbers.txt
2. Add them up
3. Handle errors
"""

#Read the file in number_file
try:
    with open("numbers.txt", "r") as number_file:
        #loop on file to read each and every line
        total = 0 #initiallizing the total
        for line in number_file:
            #introduce try..except... to handle errors
            try:
                number = int(line.strip())
                print("Read number: "+str(number))
                total = total+number
            except ValueError:
                print(line.strip()+ " is not a value")
    print(f"Total of every number present in file: {total}")
except FileExistsError:
    print("No file Exists")    


"""
this entire code that is responsible for reading and printing and addind should have been added in try block for the case of file not being found
"""