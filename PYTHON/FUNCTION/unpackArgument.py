#* and ** in function definitions to collect arguments, and use them in function calls to unpack arguments.


def display(a, b, c):
    print(a, b, c)

l1 = [10, 20, 30]
display(*l1)

#--------------------------------------------------------------------------------------

def display(name, surname):
    print(name, surname)

d1 = {"name":"abcd", "surname":"xyz"}
display(**d1)