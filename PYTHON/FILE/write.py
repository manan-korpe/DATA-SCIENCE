with open("F1.txt","w") as file: # remove old content and add new one
    file.write(input("Enter your input : "))

with open("F1.txt","r") as file:
    print(file.read())

#--------------------------------------------------------------------------------------
with open("F1.txt","a") as file: # remove old content and add new one
    file.write(input("Enter your input : "))

with open("F1.txt","r") as file:
    print(file.read())