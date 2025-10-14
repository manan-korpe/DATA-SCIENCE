# Uppercase Half String
s = "geeks for geEks"
mid = int(len(s)/2)

s = s[:mid].upper() + s[mid:].lower()
print(s)