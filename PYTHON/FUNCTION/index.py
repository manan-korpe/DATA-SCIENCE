def display():
    print("function called")

display()

def sum(n1, n2):
    return n1 + n2

print(sum(10, 30))

#Default Parameter Values
def add(n1=10, n2=11):
    print("n1 : ",n1," n2 : ",n2)

add()
add(20)
add(20,30)

# when function doesn't have body in that case pass key word is used.
def pssFunction():
    pass

# Keyword Arguments
# call a function with arguments without using keywords, they are called positional arguments.
#The order matters with positional arguments:

def display(name,surname):
    print(name, " ", surname)

display(surname="abc", name="xyz")

# making of positional and keyword arguments

display("abcd", surname="xyc")

# Positional-Only Arguments
def display(name,/):
    print(name)

display("positional argument")
# display(name = "acbc") # this gives error

def display(*, name):
    print(name)

# display("abcd") # this gives error
display(name = "keyWord argument") 

# combiation of positional and keyword arguments
def my_function(a, b, /, *, c, d):
    return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)