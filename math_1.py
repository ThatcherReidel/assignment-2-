import math

def calculate_circle(diameter):
    radius = diameter / 2
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference