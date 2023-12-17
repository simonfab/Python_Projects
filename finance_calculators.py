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

#Import libraries
import math

# Initialise variables
carry_on = True

# Define functions
def print_messages(message): # main print engine
    print(message)

def validate_integers (user_entry):  # check and convert to integer and make sure its >0
    try:
        user_entry = int(user_entry)
        if user_entry > 0:
            return user_entry
        else:
            print ("Value must be greater than 0")
            return None
    except ValueError:
        print_messages ("Invalid input - please enter a number >0")

def validate_floats (user_entry):  # check and convert to float and make sure its >0
    try:
        user_entry = float(user_entry)
        if user_entry > 0:
            return user_entry
        else:
            print ("Value must be greater than 0.0")
            return None
    except ValueError:
        print_messages ("Invalid input - please enter a number >0")

def bond_calculation(p,im,n):   # this is bond calculation - p = pv of house; im = monthly interest rate and n = no of months
    repayment = round((im*p)/(1-(1+im)**(-n)),2)
    return repayment

def simple_interest(p,r,t):   # this is simple interest - p = initial deposit, r = annual rate of interest, t= number of years
    total_amount_simple_c = round(p*(+r*t),0)
    total_interest_simple_c = total_amount_simple-p
    return total_amount_simple_c, total_interest_simple_c

                          














print("Welcome to the finance calculators.\n")

while carry_on:

    # lets get user selection, relevant inputs and process:

    init_choice = input("You can choose from:\n" + "\"Investment\" - to calculate the total amount you may earn on your investment\n" + 
                        "\"Bond\" - to calculate how much it will cost to pay off your mortgage or\n" +
                        "\"Quit\" - to terminate program\n\n" +
                        "Please enter your selection...\n")
    
    final_choice = init_choice.replace(" ","").lower()[0:4]  #process the initial choice to get consistent shortened string - this could be just 1 char given diff words
    
    if init_choice == "q":      # give the user a short cut out
        final_choice ="q"
    
    if final_choice == "quit" or final_choice =="q":    # if user wants to quit use full "quit" or short cut q
        carry_on = False

    elif final_choice =="inve":                         # deal with investment
        print("We're going to see how much you can earn by saving a lump sum...\n\n")
        print("we just need answers to a couple of easy quesions:\n")

        while True:
            #get initial deposit...in hindsight this could have been done with the house value etc in a single routine
            initial_deposit_input = input("Enter the amount you want to deposit...")
            initial_deposit = validate_integers (initial_deposit_input)
            if initial_deposit is not None:
                print (f"Your initial deposit is £{initial_deposit:,.0f}")
                break
        while True:
            #get interest rate
            int_rate_input = input("Enter the expected interest rate...")
            curr_int_rate = validate_floats (int_rate_input)
            if curr_int_rate is not None:
                monthly_int_rate = round(curr_int_rate/100/12,4)
                #curr_int_rate_extra = curr_int_rate+1
                #monthly_int_rate_extra = round(curr_int_rate_extra/100/12,4)
                print (f"Your current interest rate is {curr_int_rate}%")
                break
        while True:
            #get number of years to save
            No_of_years_input = input("Enter the expected number of years to save...")
            No_of_years = validate_floats (No_of_years_input)
            if No_of_years is not None:
                print (f"Your expected saving period is {No_of_years} years")
                break







        print (f"\nIn summary:\nAmount to deposit - £{initial_deposit:,.0f}\n"
              f"Interest rate - {curr_int_rate}% pa\n"
              f"Period to pay - {No_of_years} years\n")




































    elif final_choice == "bond":                        # deal with mortgage repayment
        print("We're going to see how much to repay your house off...\n\n")
        print("we just need answers to a couple of easy quesions:\n")

        while True:
            #get value of house - really this is the amount of money needed to pay for the house...
            curr_house_value_input = input("Enter the value of the house...")
            curr_house_value = validate_integers (curr_house_value_input)
            if curr_house_value is not None:
                print (f"Your house value is approx £{curr_house_value:,.0f}")
                break
        while True:
            #get interest rate
            int_rate_input = input("Enter the expected interest rate...")
            curr_int_rate = validate_floats (int_rate_input)
            if curr_int_rate is not None:
                monthly_int_rate = round(curr_int_rate/100/12,4)
                curr_int_rate_extra = curr_int_rate+1
                monthly_int_rate_extra = round(curr_int_rate_extra/100/12,4)
                print (f"Your current interest rate is {curr_int_rate}% or {monthly_int_rate*100}% per month") #note the monthly interest rate is rounded back up to "whole number equivalent"
                break
        while True:
            #get number of months to repay
            No_of_months_input = input("Enter the expected number of months to repay...")
            No_of_months = validate_integers (No_of_months_input)
            if No_of_months is not None:
                print (f"Your expected repayment period is {No_of_months} or {round(No_of_months/12,2)} years")
                break
        print (f"\nIn summary:\nAmount to pay - £{curr_house_value:,.0f}\n"
              f"Interest rate - {curr_int_rate}% pa\n"
              f"Period to pay - {No_of_months} months\n")
        
        #let show the results
        #first get the info from the function bond_calculation
        bond_repyament = bond_calculation(curr_house_value, monthly_int_rate,No_of_months)
        total_paid = bond_repyament*No_of_months
        total_int_paid = total_paid-curr_house_value

        #and tell the user
        print (f"The amount of the monthly bond is £{bond_repyament:,.2f}\n"
                f"The total amount payable is £{total_paid:,.2f}\n"
                f"Total interest payable is £{total_int_paid:,.2f}\n")
        
        # and see if the user wants to know what happens if interest rates go up by a point?
        show_comparison = input("Would you like to see what would happen if interest rates increased by 1%? - just enter \"y\" or \"n\"...")
        if show_comparison == "y":       #this probably needs to be handled so as to be not case sensitive
            bond_repyament_extra = bond_calculation(curr_house_value, monthly_int_rate_extra,No_of_months)
            total_paid_hr = bond_repyament_extra * No_of_months
            total_int_paid_hr = total_paid_hr-curr_house_value
            print (f"\nIf interest rates increased by just 1% to {curr_int_rate_extra}%:\n"
                    f"The amount of the increased monthly bond would be £{bond_repyament_extra:,.2f}\n"
                    f"The monthly extra payable would be £{bond_repyament_extra - bond_repyament:,.2f}\n"
                    f"Total extra interest payable would be £{total_int_paid_hr - total_int_paid:,.2f}\n\n")
       
        
        #and get ready to do it again
        print("Would you like to do another calculation...")

    else:
        print ("You have entered a nonsense! (an unrecognised string) - please try again or quit...\n\n")

# The following executes on quitting/false
print_messages(f"Thanks for using the system (carry_on = {carry_on})\n")  # This prints 'False' when 'quit is entered
