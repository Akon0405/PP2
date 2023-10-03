X1 = int(input())
Y1 = int(input())
X2 = int(input())
Y2 = int(input())
if (X2 == X1 or Y2 == Y1) or ((X2 - X1) == (Y2 - Y1) or (X2 - X1)*(-1) == (Y2 - Y1) or (X2 - X1) == (Y2 - Y1)*(-1)):
    print('YES')
else:
    print ('NO')
