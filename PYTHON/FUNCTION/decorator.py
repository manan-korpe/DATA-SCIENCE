# Decorators let you add extra behavior to a function, without changing the function's code.
# A decorator is a function that takes another function as input and returns a new function.

def changecase(func):
    def myinner():
        print("hello")
        return func()
    return myinner

@changecase
def myfunction():
    return "Hello Sally"

print(myfunction())

#--------------------------------------------------------------------------------------

def decoreFunction(func):
    def innerFun(name):
        print("inner function called")
        return func(name)
    return innerFun

@decoreFunction
def display(name):
    print("my name is ",name)

display("ABCD")

