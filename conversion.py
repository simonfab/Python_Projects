
'''
Pseudocode
Declare variables as stated
Do casting conversions
Print variables on separate lines
'''

#Declare initial variables
num1,num2,num3,string1 = [99.23,23,150,"100"]

#convert
num1 = int(num1)
num2 = float(num2)
num3 = str(num3)
string1 = int(string1)

#print on separate lines using newline as separator
print("Values as follows")
print (num1, num2, num3, string1, sep ="\n")

#print variable types to be sure
print("Variable types and values as follows:")
print (type(num1), num1)
print (type(num2), num2)
print (type(num3), num3)
print (type(string1), string1)