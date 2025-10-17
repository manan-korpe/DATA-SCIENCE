import os
if os.path.exists("F1.txt"):
  os.remove("F1.txt")
else:
  print("The file does not exist")