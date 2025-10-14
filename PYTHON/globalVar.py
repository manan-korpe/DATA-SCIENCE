x = "python"

def myfunc():
    # global x = "java" -> not work
    global x
    x = "java"
    print(x)

myfunc()
print(x)

x = "python"

#--------------------------

y = "c"
def myfunc():
    y = "rdbms"
    print(y)

myfunc()
print(y)