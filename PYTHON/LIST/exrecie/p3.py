num = [23, 34, "hello", 32, 56]

i=0
j=len(num)-1

while i<j:
    num[i],num[j] = num[j], num[i]
    i+=1
    j-=1

for n in num:
    print(n)

print(num)