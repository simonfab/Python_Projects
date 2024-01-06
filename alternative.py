'''Task 10 - alternate characters capitalised and alternate words capitalised

Student details:
#student_name = "Simon Kinsey" 
#student_number = "SK23110011962"

Notes:
pylint line length limit followed (100 chars)
note to self - research "enumerate" as this gives an automatic counter to an iterable

Pseudo code
Ask the user for a string
task part a = capitalise alternate letters starting with first char
loop through string, test if its even and capitalise lowest bound is 0
build new string
print string

task part b capitalise alternate words starting with second work
split new string into list
iterate through list 
capitalise even words (odd index)
print new string

'''

# initialise variables
new_string = ""

# ask the user for a string
user_string = input("Please enter your string..\n")

# loop through string and uppercase every other character
for i in range (len(user_string)):
    if i %2 == 0:
        new_string += user_string[i].upper()
    else:
        new_string += user_string[i].lower()
# print new string
print (f"Every other letter capitalised: \" {new_string}\"\n")


# now capitalise every even whole word
# split the string into a list
new_string_list = new_string.split()

# print(new_string_list)

# loop through list and uppercase every even word
for i in range (len(new_string_list)):
    if i %2 == 1:
        new_string_list[i] = new_string_list[i].upper()
    else:
        new_string_list[i] = new_string_list[i].lower()

# create new string with spaces between evenly capitalised words
new_string = str(" ".join(new_string_list))

# print new string
print (f"Every even word capitalised: \" {new_string}\"\n")
