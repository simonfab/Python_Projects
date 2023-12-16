'''
Student details:
#student_name = "Simon Kinsey" 
#student_number = "SK23110011962"
'''

#get user input - in one input string

numbers_input = input("Please enter your 3 numbers separated by spaces...")
numbers_list = numbers_input.split()
print (numbers_list)

# now i need to convert to integers
# it really should be done by manipulating the list but im not sure how to do that
# and there should be checks on integer values and a count of 3 items
# so for now:

num1 = int(numbers_list[0])
num2 = int(numbers_list[1])
num3 = int(numbers_list[2])


#print the sum of the three numbers (and store the sum for later)
total = num1 + num2 + num3
answer = total
print (f"The sum of the three numbers is {answer}")

#print the first number minus the second number
answer = num1 - num2
print (f"{num1} - {num2} = {answer}")

#print the third number multiplied the first number
answer = num3 * num1
print (f"{num3} * {num1} = {answer}")

#print sum of all 3 divided by the third number
answer = round((total / num3),2)
print (f"{total} / {num3} = {answer}\n")
