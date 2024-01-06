'''Task 09 - Defensive programming practical task 1 part 2 - fix errors2.py

Student details:
#student_name = "Simon Kinsey" 
#student_number = "SK23110011962"

Notes:
    using pylint guide for 100 chars for line length, but as the instruction said to add a comment to each line I have not broken the "fix comment to more than one line"
    still not sure about the pylint error about "Constant name... doesnt conform to UPPER_CASE etc"
'''

# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "lion"                 # fixed with inverted commas for string and decapitalising (as its not a proper noun)
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth." # fixed by converting to f string, putting in animal type and correcting variable for teeth number

print (full_spec)               # fixed with paretheses
