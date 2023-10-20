import math

def sphere_volume(radius):
    if radius < 0:
        return "Radius cannot be negative"
    else:
        volume = (4/3) * math.pi * (radius**3)
        return volume

radius = 7.0
print("The volume of the sphere with radius", radius, "is", sphere_volume(radius))
