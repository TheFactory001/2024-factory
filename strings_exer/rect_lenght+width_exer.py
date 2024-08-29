#4. Write a program that takes the length and width of a rectangle as input (both floats) and calculates its perimeter.
l = float(input("Enter the length: "))
w = float(input("Enter the width: "))

perimeter_of_rectangle = 2 * (l + w)
q = (l + l) + (w + w)

print("The primeter of the rectangle is",perimeter_of_rectangle)