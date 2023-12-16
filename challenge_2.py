'''
Task 02 - challenge_2

Student details:
#student_name = "Simon Kinsey" 
#student_number = "SK23110011962"
'''

'''
pseudo code
get the name of users favoured restaurant
get the users favourite number 
cast fav number to an int
print
try and cast the restaurant to an int get an error and explain
'''


string_fav = input("Please enter your favourite restaurant...")
int_fav = input("enter your favourite number...")

#cast int_fav to an int (from a string)
int_fav = int(int_fav)

print (string_fav)
print (int_fav)

print()
print("now for casting a string to an int!!")

string_fav = int(string_fav)

# this will generate a valueError as you can't cast a string to an int