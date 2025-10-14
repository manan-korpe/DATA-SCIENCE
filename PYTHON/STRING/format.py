name = "abcd"
nmber = 123

print(f"Hello {name}, your number is {nmber}")
print("Hello {}, your number is {}".format(name, nmber))
print("Hello {1}, your number is {0}".format(nmber, name))
print("Hello {n}, your number is {num}".format(n=name, num=nmber))
