# python has several functions for creating , reading , updating , and deleting files(CRUD)
# The KEY function for working with files is open().
# The open () function takes two parameters: filename and mode.
# modes for opening a file
# "r"- Read
# "a"- Append
#"w"- write
# "x" - create
try:
    f = open("text.html", "w")
except:
    print("text.txt file does not exist")

try:
    f = open("index.py", "x")
except:
    print("text.txt file does not exist")

# creating and writing files
# f = open("myfile.txt", "x")

f = open("my_file.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("my_file.txt", "r")
print(f.read())











