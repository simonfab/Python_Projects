'''
Task 02 - challenge_1

Student details:
#student_name = "Simon Kinsey" 
#student_number = "SK23110011962"
'''

'''
pseudo code
Import maths code
Define a function for area of a triangle
Ask the user for 3 side lengths of triangle (could test if its a valid triangle)
Check they are numbers (could check that they are not negative)
Ask the user for level of precision required - ie number of decimal places
Calculate area of triangle using herons rule to level of precision required by user
Print area of triangle for user
'''
# import math library
import math

# define a function for area of a triangle
def calc_area_triangle (side1, side2, side3, precision):
    perim = side1+side2+side3
    s= perim/2  
    return round(math.sqrt(s*(s-side1)*(s-side2)*(s-side3)),precision)
    
try:
    u_side1 = float(input("Enter length of side 1:  "))
    u_side2 = float(input("Enter length of side 2:  "))
    u_side3 = float(input("Enter length of side 3:  "))
    u_precision = int(input("Enter precision (no of decimal places for answer):  "))
    area = calc_area_triangle(u_side1,u_side2,u_side3,u_precision)
    print(f"The area of the triangle is {area} to {u_precision} dps")
except ValueError:
    print("One or more of the inputs is not a number - please start again..")








