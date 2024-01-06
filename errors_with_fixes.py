# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program")  # fixed by adding parentheses
print ("\n")                            # fixed by removing indent and adding parentheses = though this "\n" could have been in previous line

# Variables declaring the user's age, casting the str to an int, and printing the result
age_str = "24"                          # fixed by removing indent, changing "==" to "=", decapitalising the s in Str, removing the non numeric text from the string 
age = int(age_str)                      # fixed by removing indent, decapitalsing the S to match
print("I'm " + str(age) + " years old.")# fixed by adding space after "m" and before "y", converting "age" int back to a string

# Variables declaring additional years and printing the total years of age
years_from_now = 3.5                    # removed indent and inverted commas to treat years from now as float and increased value to 3.5 to allow for additional 6 months
total_years = age + years_from_now      # removed indent

print ("The total number of years: " + str(total_years)) #"answer_years") # fixed by adding parentheses for print, using correct varible total years which needs to be converted to a string to concatenate

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12         # fixed by changing calculation to use total_years
#print (total_months)
print ("In 3 years and 6 months, I'll be " + str(total_months) + " months old") # fixed by adding parentheses and converting total_months to string

#HINT, 330 months is the correct answer
