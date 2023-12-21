'''Task 08 - pattern.py - output the specified * pattern

Student details:
#student_name = "Simon Kinsey" 
#student_number = "SK23110011962"

Pattern required for 9 rows is
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
pattern with 1 star
ask the user for the number of rows to print (max interations +1 for loop)
calculate the halfway point
do the printing loop
    decide what to print ie whether its met the half way point or not
    to start decreasing the number of stars
    print the row
end
'''


# Declare variables
counter = 0
pattern ="*"


# Opening message
print ("Welcome to the \"pattern\" printer:\n")

# get user input
# calculate halfway point
rows = int (input ("How many rows would you like print? Odd numbers"
                   " please, like 9!..."))
halfway = int (round (rows/2,0)+1)
print ()

# loop to print the pattern
for counter in range (1,rows+1):

    # if less than half way print the pattern for the
    #numbers of rows so far:
    if counter <= halfway:
        print (f"{pattern * counter}")

    # if its more than half way decrease the halfway counter
    #and use that to print the number of stars:
    else:
        halfway -=1
        print (f"{pattern * halfway}")
