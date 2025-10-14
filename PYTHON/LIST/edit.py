l1 = ["a", "b", "c" , "c", 10, 2.5, True]
l1[0] = "x"
print(l1)

l1 = ["a", "b", "c" , "c", 10, 2.5, True]
l1[:3] = ["p", "q", "r"]
print(l1)

l1 = ["a", "b", "c" , "c", 10, 2.5, True]
l1[2:4] = [20, 30, 40]
print(l1)

l1 = ["a", "b", "c" , "c", 10, 2.5, True]
l1[2:4] = [10]
print(l1)

l1 = ["a", "b", "c" , "c", 10, 2.5, True]
l1[2:4] = []
print(l1)

l1 = ["a", "b", "c" , "c", 10, 2.5, True]
l1.append("new")
print(l1)

l1 = ["a", "b", "c" , "c", 10, 2.5, True]
l1.insert(2, "new")
print(l1)

l1 = ["a", "b", "c" , "c", 10, 2.5, True]
l1.extend(["x", "y", "z"])
print(l1)

l1 = ["a", "b", "c" , "c", 10, 2.5
, True]
l1.remove("c")
l1.pop()
l1.pop(2)
del l1[0]
print(l1)

l1.clear()
print(l1)