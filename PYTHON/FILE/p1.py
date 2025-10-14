import os

try:
    file = open("F1.txt","r")
    print(file.read())
    file.close()
except:
    print("Something want wrong")

# print("Current working directory:", os.getcwd())

