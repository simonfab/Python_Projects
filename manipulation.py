'''
Student details:
#student_name = "Simon Kinsey" 
#student_number = "SK23110011962"
'''

# get user string
str_manip = input("Please enter your string...")


#calculate and print length of string
length = len(str_manip)
print (f"The length of the string is {length}")

#Get the last character
last_character = str_manip[length-1]
char_to_replace = last_character # would allow other characters to be replaced by changeing index stored in char to replace
print (f"The character to replace is '{char_to_replace}'")

#and replace the last char with @signs and store it in a sep variable to preserve original input and print it
str_manip_1 = str_manip.replace(char_to_replace,"@")
print (str_manip_1)

#print the last 3 characters backwards
print(str_manip[-3:][::-1])

#make a new five letter word made up of the first 3 characters and the last 2 characters of entered phrase
new_word=str_manip[:3]+str_manip[-2:]
print (new_word)















