'''
Task 05 - Capstone Project - finance calcuators

Student details:
#student_name = "Simon Kinsey" 
#student_number = "SK23110011962"

Pseudo code
import libraries
    math

define functions:
    get choice
        validate including making allowances for caps etc
        call appropriate function
            end
            bond
                call bond input and calc message
            investment
                determine if they want simple or compound    
                call correct interest function
        end option
            set continue to false
            set message to goodbye
    bond option input
        get data and validate (positive floats or ints as approp)
        call bond calc function
    simple interest input
        get data and validate (positive floats or ints as approp) could this be the same funtion as for bond?
        call simple interest calc
    compound interest input
        get data and validate (positive floats or ints as approp) could this be the same funtion as for bond and simple?
        call compound interest calc
    bond calculator
        basic forumla = repayment = (i*p)/(1-(1+i)**(-n))
    simple interest calculator
        basic forumla = A = P*(1+r*t)
    compound interest calculator
        basic forumla = A=P*math.pow(((1+r),t)

if investment:
    ask for inputs of 
    rate of interest (float?)
    no of whole years to invest (int)
    simple or compound return required (could be a boolean but use an int to allow for other options in future)
    do the calculations using the defined funcitons and calculate return messages
    validate inputs especially completeness and greater than 0
    printout the answer - assume - depost, interest earned, and total amt incl interest
    perhaps do a comparison option 
if bond:
    ask for inputs of
    house value (int)
    rate of interest (float?)
    number of months to repay (int)
    validate inputs especially completeness and greater than 0
    do the calculations using the defined function and calculate return messages
    printout the answer - assume - no of months to repay, total repaid, interest paid
    perhaps do a comparison option
print messages'''

# Initialise variables
carry_on = True

# Define functions
def print_messages(message):
    print(message)

print("Welcome to the finance calculators - enter your selection")

while carry_on:
    init_choice = input("Please select from \"bond\", \"savings\" or \"quit\" (to terminate program)")
    print(init_choice)
    final_choice = init_choice[1:3].lower()
    print (f"final_choice is {final_choice})
   
    if init_choice == "quit":
        carry_on = False
    

    #else:
     #   print("You have entered an unrecognised string please try again or enter quit...")

# The following statements are outside of the while loop
print_messages(f"Thanks for using the system (carry_on = {carry_on})")  # This prints 'False' when 'quit is entered