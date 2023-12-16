'''
Student details:
#student_name = "Simon Kinsey" 
#student_number = "SK23110011962"
'''

#delcare initial phrase
phrase = "The!quick!brown!fox!jumps!over!the!lazy!dog."

#replace exclamation marks with spaces
phrase = phrase.replace("!"," ")
print (phrase)

#print the upper case version of phrase
#phrase = phrase.upper
print (phrase.upper())

#print phrase in reverse
print (phrase[::-1])

#or for the upper case version in reverse (phrase not updated)
print(phrase.upper()[::-1])
