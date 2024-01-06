'''Task 09 - optional challenge

Student details:
#student_name = "Simon Kinsey" 
#student_number = "SK23110011962"

Notes:
    pylint line lenght limit followed (100 chars)

Pseudo code
Ask the user for a name
print the name
print the number of characters
split the name into its component words
Show the list of words that make up the name and how many words
get the last word(s) to be last name
print caclulated last name - this is where the logic problem is ..
- it calculates last name as last 2 words but its too coarse to allow for all user entries so corrected version uses 
just last word which allows for hyphens but not double barrelled names without hyphens

'''

# incorrect version:
name_string = Input("Please enter your full name...\n") # capital I on input
print(ame_string)                                      # incorrect spelling of name_string variable - ie NameError - should be f string too
name_len = len (name_string)
    print (name_len)                                    # unexpected indent
sep_string = name_string.split("")                     # separator should have a space
sep_len = len(sep_string)
print ("Entire name is " + sep_string + name_len)  #(name_len is an int and needs to be str - actually should be an f string etc - see below)
last_name_test = sep_string [sep_len+1]  # out of range error
last_name = " ".join(sep_string [-2:])    # logic error - if the user enters a 2 word name or a "hyphenated last name" eg Winstone-smith it doesnt give the correct last name...
print(last_name)

'''
# Correct version:
# The correct version appears below (but still with logic error which would require a lot more coding...)

name_string = input("Please enter your full name...\n")
print (f"Your full name is {name_string}")

name_len = len (name_string)
print (f"There are {name_len} characters in your name")

sep_string = name_string.split(" ")

sep_len = len(sep_string)

print (f"Entire name is {sep_string} - {sep_len} words") # (name_len is an int and needs to be str)

last_name = " ".join(sep_string [-1:])

print(f"Last name is {last_name}")
'''
