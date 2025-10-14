num = [2,3,2,4,7,8]

if len(num) == 0:
    print("Your num length is zero")
else:
    max = num[0]
    for i in range(1,len(num)):
        if num[i] > max:
            max = num[i]
        else:
            pass

    print(max)