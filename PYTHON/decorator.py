def log(func):
    def wrapper(a,b):
        print("decorator called")
        func(a,b)
        print("decorator finised")
    return wrapper

@log
def sum(a, b):
    print(a+b)

sum(10,20)