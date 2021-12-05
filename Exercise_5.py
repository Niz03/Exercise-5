# Write a program that accepts the lengths of three sides of a triangle as inputs. The program output should indicate whether or not the triangle is an equilateral triangle.

print("\n**************************************************************\n***** Hello! Welcome to my Equilateral Triangle Checker! *****\n**************************************************************\n")






sideA = input("enter the first angle of the triangle: ")
sideB = input("Now please enter the second angle of the triangle: ")
sideC = input("Finally, enter the last angle of the triangle: ")

if sideA == sideB and sideB == sideC:
    print("\nYour triangle is an equilateral one.\n")
else:
    print("\nYour triangle is not an equilateral one.\n")