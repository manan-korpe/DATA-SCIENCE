# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

try:
    file = open("F1.txt","rb")
    print(file.read()) # read entire file binaray
    file = open("F1.txt","rt")
    print(file.read()) # read entire file text
    
    file.close() # must close after worked with file for buffer free and changes visable after editing file 
except:
    print("Something want wrong")

# print("Current working directory:", os.getcwd())

