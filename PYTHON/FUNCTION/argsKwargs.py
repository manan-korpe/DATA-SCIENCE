#args variable length arguments
def display(*args):
    print(args)
    print(type(args))

display(10,20,30,40,50,"accd",True)

#--------------------------------------------------------------------------------------

# Arbitrary Keyword Arguments  **kwargs
def display(**kwargs):
    print(kwargs)
    print(type(kwargs))

display(name="mk", surname="abd")

#--------------------------------------------------------------------------------------

# combine *args **kwargs
def display(*args, **kwargs):
    print(args)
    print(kwargs)

display(10, 20, 30, a="a", b="b", c="x")