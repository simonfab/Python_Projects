'''Task 07 - while.py - while loop and average

Student details:
#student_name = "Simon Kinsey" 
#student_number = "SK23110011962"

Pseudo code
Declare variables for:
    - a counter so that know how many numbers have been entered
    - a running total
    - a list to store the entered numbers in
    - an average to store the averge in - in case you want to use it in the future

Declare functions
    seeing as this is simple for using an infinite while loop I wont be declaring any functions
        - validations
        - calculations

while true loop to keep asking the user for numbers
Ask the user for a number (presumably any float will be ok for the purposes, positive or negative)
give them the option to end and print message including list, average and count
append the number to a list
otherwise add 1 to the counter
add the number to a running total'''


# Declare variables
counter = 0
average = 0
user_numbers = []
total_numbers = 0

# Opening message
print ("welcome to the \"average\" calculator:")

while True:
    user_input = input("Please enter your number or \"end\" to end and print your results...")
    if user_input == "end":
        if counter ==0:
            print ("You didn't enter any numbers :(")
            break
        else:
            total_numbers = sum(user_numbers)
            average = round (total_numbers/len(user_numbers),2) # could have used counter
            print (f"\nThe numbers you entered are: {user_numbers}\n"
                f"You entered {counter} numbers\n"
                f"The total is {total_numbers}.\n"
                f"The average of your set of numbers is {average} (to 2 decimal places)")
        break
    else:
        try:
            user_input = float (user_input)
            counter +=1
            user_numbers.append (user_input)
        except ValueError:
            print ("Invalid input - please enter a number...")
