"""
Task 03

Student details:
#student_name = "Simon Kinsey" 
#student_number = "SK23110011962"

Pseudo code
get the users age - probably should test for not 0, store as int
if over 100 - dead
elif 65 or over - retirement
elif 40 or over - over the hill
elif = 21 - congrats
elif under 13 - kiddie disc
else - age is but a number
"""

#get age
age = int(input("Please enter your age..."))

#tests and message calc...
if age > 100:
    message = "Sorry you're dead!"
elif age >= 65:
    message = "Enjoy your retirement!"
elif age >= 40:
    message = "You're over the hill :("
elif age == 21:
    message = "Congrats on your 21st!"
elif age < 13:
    message = "You qualify for the kiddie discount :)"
else:
    message = "Age is but a number"
print (f"You are {age} - {message}")






