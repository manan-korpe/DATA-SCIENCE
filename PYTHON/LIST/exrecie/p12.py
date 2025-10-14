n = int(input("Enter total no of element do you want to insert: "))
num = []

while n>0:
    el = int(input("Enter element: "))
    num.append(el)
    n-=1

print("Your num array is: ", num)