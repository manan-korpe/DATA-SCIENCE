# check whether the string is Symmetrical or Palindrome

def isSymmetrical(str):
    mid = int(len(str)/2)
    print("Symmetrical" if str[:mid] == str[mid:] else "Not Symmetrical")


def isPlindrome(str):
    print("Palindrome" if str == str[::-1] else "Not Palindrome")


s = "ab"
isSymmetrical(s)
isPlindrome(s)

s = "abaaba"
isSymmetrical(s)
isPlindrome(s)
