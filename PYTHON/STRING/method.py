str = "this is string example"

print("capitalize     :", str.capitalize())       # Capitalizes first letter
print("upper          :", str.upper())            # Converts entire string to uppercase
print("lower          :", str.lower())             # Converts entire string to lowercase
print("title          :", str.title())            # Capitalizes first letter of each word
print("strip          :", str.strip())            # Removes leading/trailing whitespace
print("replace        :", str.replace("s", "X"))  # Replaces all 's' with 'X'
print("split          :", str.split(" "))         # Splits string at spaces and returns list

print("count 't'      :", str.count("t"))         # Counts number of 't' in string

# Tabs
str = "this \tis \tstring example"
print("expandtabs(2)  :", str.expandtabs(2))      # Expands tabs to 2 spaces
print("expandtabs(8)  :", str.expandtabs(8))      # Expands tabs to 8 spaces

# Indexing
print("index('is')    :", str.index("is"))        # Finds first occurrence of 'is'
print("rindex('is')   :", str.rindex("is"))       # Finds last occurrence of 'is'

# Finding (similar to index but doesn't raise error if not found)
print("find('is')     :", str.find("is"))         # First occurrence
print("rfind('is')    :", str.rfind("is"))        # Last occurrence (← this is the function you meant: **rfind**)

# Alphanumeric checks
str = "this"
print("isalpha        :", str.isalpha())          # True if all letters
print("isdigit        :", str.isdigit())          # True if all digits
print("isalnum        :", str.isalnum())          # True if all alphanumeric (no symbols or spaces)

# Joining a tuple
tuple1 = ("a", "b","w", "Z")
print("join with 'this':", str.join(tuple1))      # Joins tuple elements with "this" between them
