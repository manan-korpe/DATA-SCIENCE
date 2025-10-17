with open("F1.txt","r") as file:
    print("3 word read--------------")
    print(file.read(3))

with open("F1.txt","r") as file:
    print("all line read--------------")
    print(file.read())

with open("F1.txt","r") as file:
    print("1 line read--------------")
    print(file.readline())

with open("F1.txt","r") as file:
    print("Read entire file line by line using only loop-----------------")
    for f in file:
        print(f)