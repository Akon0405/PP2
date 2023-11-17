import os
if os.path.exists("B"):
  os.remove("B.txt")
else:
  print("The file does not exist")