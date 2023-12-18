'''Task 05 - Capstone Project - finance calcuators

Student details:
#student_name = "Simon Kinsey" 
#student_number = "SK23110011962"

Pseudo code
import libraries
    math

define functions:
    print message
        this was supposed to be standard function for printing calculated message but in the end most
        printing was done in line
    validate_integers 
        a standard routine that checks entry for valid integer in this case greater than 0
    validate_floats
        a standard routine that checks entry for valid float in this case greater than 0
    bond_calculation
        p = pv of house; im = monthly interest rate and n = no of months
        basic forumla = repayment = (i*p)/(1-(1+i)**(-n))
        returns monthly repayment
    interest_calculations
        does both simple and compound calculations
        takes deposit, interest rate and period to save
        simple interest calculator - basic forumla = A = P*(1+r*t)
        compound interest calculator - basic forumla = A=P*math.pow(((1+r),t)
        returns total amount returned and interest earned (4 outputs)

    get choice (main loop)
        validate for valid string lower case and shorten
        q/quit ends
        i/investment for savings
        b/bond for bond

        if investment:
            ask for inputs of 
                amount to deposit (int) and validate
                rate of interest (float) and validate
                no of years to invest (float) and validate
            run the calcs
            ask the user what they want to see
                simple/s
                    show simple int results
                compound/c
                    show compount interest results
            if bond:
            ask for inputs of
                house value (int) and validate
                rate of interest (float) and validate
                number of months to repay (int) and validate
                do the calculations using the defined function and calculate return messages
                offer a comparison option
                    does the user want to see the effect of a 1% increase in interest rates
                        if yes
                            calculate new interest rates
                            re-run function
                            show a message that shows increase in costs
    print messages
    end'''

# Import libraries
import math

# Define functions

def print_messages(message):
    '''main print engine - prints supplied message'''
    print(message)

def validate_integers (user_entry):
    '''validate_integers - standard function to recieve input, try to convert to integer and that its greater than 0
       returns integer - otherwise returns none'''
    try:
        user_entry = int(user_entry)
        if user_entry > 0:
            return user_entry
        else:
            print ("Value must be greater than 0")
            return None
    except ValueError:
        print_messages ("Invalid input - please enter a number >0")

def validate_floats (user_entry):
    '''validate_floats - standard function to recieve input, try to convert to float and entry is greater than 0
       returns float - otherwise returns none'''
    try:
        user_entry = float(user_entry)
        if user_entry > 0:
            return user_entry
        else:
            print ("Value must be greater than 0.0")
            return None
    except ValueError:
        print_messages ("Invalid input - please enter a number >0")

def bond_calculation (p,im,n):
    '''bond_calculation - p = pv of house; im = monthly interest rate and n = no of months
       returns monthly repayment'''
    repayment = round((im*p)/(1-(1+im)**(-n)),2)
    return repayment

def investment_calculation (p,r,t):
    '''investment interest calucator - p = initial deposit, r = annual rate of interest, t= number of years
       returns simple and compound interest and total interest earned'''
    # simple
    tot_amt_simp_c = round(p*(1+r*t),0)
    tot_int_simp_c = tot_amt_simp_c-p
    # compound
    tot_amt_comp_c = round(p*math.pow((1+r),t),0)
    tot_int_comp_c = tot_amt_comp_c-p
    return tot_amt_simp_c, tot_int_simp_c, tot_amt_comp_c, tot_int_comp_c

# main code loop follows

print ("\nWelcome to the finance calculators.\n")

while True:
    # lets get user selection, relevant inputs and process:

    init_choice = input("You can choose from:\n" + "\"Investment\" - to calculate the total amount you may earn on your investment\n"
                        + "\"Bond\" - to calculate how much it will cost to pay off your mortgage or\n"
                        + "\"Quit\" - to terminate program\n\n"
                        + "Please enter your selection...\n")

    final_choice = init_choice.replace(" ","").lower()[0:4]  #process the initial choice to get consistent shortened string - this could be just 1 char given diff words

    if final_choice == "quit" or init_choice =="q":    # if user wants to quit use full "quit" or short cut q
        break #carry_on = False

    elif final_choice =="inve" or init_choice =="i":                         # deal with investment
        print("We're going to see how much you can earn by saving a lump sum...\n\n")
        print("we just need answers to a couple of easy quesions:\n")

        while True:
            # get initial deposit...in hindsight this could have been done with the house value etc in a single routine
            initial_deposit_input = input("Enter the amount you want to deposit...")
            initial_deposit = validate_integers (initial_deposit_input)
            if initial_deposit is not None:
                print (f"Your initial deposit is £{initial_deposit:,.0f}")
                break
        while True:
            # get interest rate to 4dps
            int_rate_input = input("Enter the expected interest rates...")
            curr_int_rate = validate_floats (int_rate_input)
            if curr_int_rate is not None:
                curr_int_rate = round(curr_int_rate/100,4)
                print (f"Your current interest rate is {curr_int_rate*100:,.2f}%")
                break
        while True:
            # get number of years to save
            No_of_years_input = input("Enter the expected number of years to save...")
            No_of_years = validate_floats (No_of_years_input)
            if No_of_years is not None:
                No_of_years = round(No_of_years,2)
                print (f"Your expected saving period is {No_of_years} years")
                break

        print (f"\nIn summary:\nAmount to deposit - £{initial_deposit:,.0f}\n"
              f"Interest rate - {curr_int_rate*100:,.2f}% pa\n"
              f"Period to save - {No_of_years} years\n")

        # call the caluclations
        total_simp_ret, total_simp_int, total_cum_ret, total_cum_int = investment_calculation(initial_deposit, curr_int_rate, No_of_years)

        # ask the user what result they would like to see
        while True:
            user_int_choice = input("You can choose to see the results on two different calucations - choose from:\n" 
                                    + "\"Simple\" - to see the total amount returned from simple interest calculation or\n"
                                    + "\"Compound\" - to calculate how much it will cost to pay off your mortgage\n"
                                    + "\"Move on\" to do some more calculations...\n")

            user_int_choice_final = user_int_choice.replace(" ","").lower()[0:4]  #process the initial choice to get consistent shortened string

            if user_int_choice_final == "simp" or user_int_choice =="s":    # show simple results (s is the short cut)
                print (f"The simple amount returned after {No_of_years:,.2f} years will be £{total_simp_ret:,.0f}\n"
                       f"The simple interest earned would be £{total_simp_int:,.0f}\n")
            elif user_int_choice_final == "comp" or user_int_choice =="c":
                print (f"The compound amount returned after {No_of_years:,.2f} years will be £{total_cum_ret:,.0f}\n"
                       f"The compound interest earned would be £{total_cum_int:,.0f}\n")
            else:
                break


  # Deal with bond calculation

    elif final_choice == "bond" or init_choice =="b":       # deal with mortgage repayment (short cut is 'b')
        print("We're going to see how much to repay your house off...\n\n")
        print("We just need answers to a couple of easy quesions:\n")

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
                print (f"Your current annual interest rate is {curr_int_rate}% ")
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

        # let show the results
        # first get the info from the function bond_calculation
        bond_repyament = bond_calculation(curr_house_value, monthly_int_rate,No_of_months)
        total_paid = bond_repyament*No_of_months
        total_int_paid = total_paid-curr_house_value

        # tell the user
        print (f"The amount of the monthly bond is £{bond_repyament:,.2f}\n"
              f"The total amount payable is £{total_paid:,.2f}\n"
              f"Total interest payable is £{total_int_paid:,.2f}\n")

        # see if the user wants to know what happens if interest rates go up by a point?
        show_comparison = input("Would you like to see what would happen if interest rates increased by 1%? - just enter \"y\" or \"n\"...")
        if show_comparison == "y":       #this probably needs to be handled so as to be not case sensitive
            bond_repyament_extra = bond_calculation(curr_house_value, monthly_int_rate_extra,No_of_months)
            total_paid_hr = bond_repyament_extra * No_of_months
            total_int_paid_hr = total_paid_hr-curr_house_value
            print (f"\nIf interest rates increased by just 1% to {curr_int_rate_extra}%:\n"
                  f"The amount of the increased monthly bond would be £{bond_repyament_extra:,.2f}\n"
                  f"The monthly extra payable would be £{bond_repyament_extra - bond_repyament:,.2f}\n"
                  f"Total extra interest payable would be £{total_int_paid_hr - total_int_paid:,.2f}\n\n")

# get ready to do it again
        print ("Would you like to do another calculation...")

# inital string result nonsensical
    else:
        print ("You have entered nonsense! (an unrecognised string) - please try again or quit...\n\n")

# The following executes on quitting/break
print_messages ("Thanks for using the system")  # This prints 'False' when 'quit is entered
