# Program to count number of lines in this files
# Opening a file
file = open("Activity 2/Aboutcars.txt","r")
Counter = 0

# Reading from file
Content = file.read()
# spliting content into lines
# and storing them in a list
Colist = Content.split("\n")

for i in Colist:
    if i:
        Counter +=1

print("This is the number of lines in the file")
print(Counter)