'''Task 08 - pattern.py - output the specified * pattern

Student details:
#student_name = "Simon Kinsey" 
#student_number = "SK23110011962"

Pattern is
*
**
***
****
*****
****
***
**
*



Pseudo code
Declare variables for:
counter
pattern 1
'''


# Declare variables
counter = 0
pattern ="*"


# Opening message
print ("welcome to the \"pattern\" printer:\n")

rows = int (input ("how many rows to print?"))
halfway = int (round (rows/2,0))

print(f"{rows} {halfway}\n",)



                  


#main loop to print the pattern



for counter in range (1,rows+1):
    if counter <= halfway:
        print (f"{pattern * counter} {counter} {halfway}")
    else:
        halfway -=1
        print (f"{pattern * halfway} {counter} {halfway}")
9

''' use the half way counter in reverse'''
