import math

def polygon_area(n, l):
    Area = (n*l**2)/(4*math.tan(math.pi/n))
    return Area

n = int(input("Enter a number of sides:"))
l = float(input("Enter a lenght of sides:"))

print(polygon_area(n, l))
