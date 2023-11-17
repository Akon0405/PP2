import os
print('Exist:', os.access('C:/Users/akonp/OneDrive/Рабочий стол/python', os.F_OK))
print('Readable:', os.access('C:/Users/akonp/OneDrive/Рабочий стол/python', os.R_OK))
print('Writable:', os.access('C:/Users/akonp/OneDrive/Рабочий стол/python', os.W_OK))
print('Executable:', os.access('C:/Users/akonp/OneDrive/Рабочий стол/python', os.X_OK))