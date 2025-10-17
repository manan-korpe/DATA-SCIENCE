number = int(input("Enter number : "))
div =int(input("Enter deviser : "))
try:
    val = number/div
    print("ans is : ",val)
except:
    print("something want wrong")
else:
    print("every thing is good")
finally:
    print("terminat the code......")