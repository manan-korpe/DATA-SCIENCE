s = "hello world"
t1 = s.split(" ")

for i in range(len(t1)):
    word = t1[i]
    if len(word) == 1:
        # Capitalize single-character word
        t1[i] = word.upper()
    else:
        # Capitalize first and last character
        t1[i] = word[0].upper() + word[1:-1] + word[-1].upper()

# Join the transformed words back into a string
s = " ".join(t1)
print(s)
