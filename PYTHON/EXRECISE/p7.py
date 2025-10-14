#  Accept the Strings Which Contains all Vowels

def isVowel(s):
    v = 'aeiou'

    for c in s:
        if c not in v:
            print("not Vowels")
            return
        
    print("all Vowels")

s = "iouaes"
isVowel(s)