import os
print("Test a path exists or not:")
path = r'C:/Users/akonp/OneDrive/Рабочий стол/python'
print(os.path.exists(path))
path = r'C:/Users/akonp/OneDrive/Рабочий стол/python'
print("\nFile name of the path:")
print(os.path.basename(path))
print("\nDir name of the path:")
print(os.path.dirname(path))