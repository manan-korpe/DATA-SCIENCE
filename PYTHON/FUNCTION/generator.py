# Generators are functions that can pause and resume their execution.
# it returns a generator object, which is an iterator.
# yield is used inside generator function 
# Generators are memory-efficient because they generate values on-the-fly instead of storing everything in memory

def genFunction(val):
    for i in range(1, val, 2):
        yield i

makeLoop = genFunction(1000)

print(next(makeLoop))
print(next(makeLoop))
print(next(makeLoop))
print(next(makeLoop))

def genName():
    yield "a"
    yield "b"
    yield "c"

names = genName()

print(next(names))
print(next(names))
print(next(names))
# print(next(names))  # This will raise StopIteration

#--------------------------------------------------------------------------------------

# List comprehension - creates a list
list_comp = [x * x for x in range(5)]
print(list_comp)

# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp))

#--------------------------------------------------------------------------------------

# send()
def echo_generator():
  while True:
    received = yield # get argument value
    print("Received:", received)

gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello")
gen.send("World")
next(gen)

#--------------------------------------------------------------------------------------

# close() function close the generator
def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
print(next(gen))
gen.close()