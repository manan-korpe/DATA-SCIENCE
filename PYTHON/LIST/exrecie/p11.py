num = [2, 23, 24, 51, 46, 67]
odd =  []
even = []

for n in num:
    if n%2==0:
        even.append(n)
    else:
        odd.append(n)

print(odd,even)
