num = ["Hello", 34, 45, "", 40]
ans = []

for n in num:
    if n != "":
        ans.append(n)

num = ans
print(num)

num = ["Hello", 34, 45, "", 40]

while "" in num:
    num.remove("")

print(num)