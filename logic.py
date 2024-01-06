'''Task 09 - Defensive programming practical task 2 - logic.py

Student details:
#student_name = "Simon Kinsey" 
#student_number = "SK23110011962"

Notes:
    from experience i know that date formatting/date handling can be problematic in all languages

    all this program does is tell the user whether a date is in the future or in the past
    but if you enter todays date it will tell you in the future becuase of the use of the "less than" operator
    
    if you were trying to summarise say sales transactions - this would create a critical logic failure...

    I had to use datetime module to make this work - which was a new experience
    using pylint guide for 100 chars for line length
    still not sure about the pylint error about "Constant name... doesnt conform to UPPER_CASE etc"
'''


# import date and datetime from datetime
from datetime import date, datetime

# set up todays date and format (the format string could be held in a constant but not done here)
today = date.today()
today_f = today.strftime("%d/%m/%y")

# get user input
# nb not doing any validation on this for the purposes of this exercise
user_date = input ("Please enter your date in the format dd/mm/yy\n")

# convert user date to a date and format as a date for messages
date_to_test = datetime.strptime (user_date,"%d/%m/%y").date()
date_to_test_f = date_to_test.strftime("%d/%m/%y")

# print a summary of the task for the user
print (f"The date you wish to test is {date_to_test_f} and today's date is {today_f}")

# test the user entered date vs todays date - and make the logic error
# nb i have used an elif to make it even more explicit
# if the user enters today's date it will not be considered and the program will end
if date_to_test < today:
    print(f"{date_to_test_f} is in the past")
elif date_to_test > today:
    print(f"{date_to_test_f} is in the future")
