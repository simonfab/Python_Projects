'''
- ask user for name, age, house number and street name with an appropriate prompt - entries to be split by commas
- store in 4 variables (name, age, house_number, street_name)
- a check to see that 4 variables have been entered - i think this is try/except but Im not sure if this is best way
- preferably in a single command clean the entries up so that extraneous spaces are removed and age is treated as an integer
- print the sentence "this is name. he is x years old and lives at house number on x street"
'''


#get and check data and if ok print the sentence
try:
    name, age, house_number, street_name = input("Please enter your name, age, house number, and street name separated by commas (e.g., 'Simon Kinsey, 61, 27, The Crescent')...").split(",")
    cleaned_name = ' '.join(name.strip().title().split())
    age = int(age.strip())
    cleaned_house_number = house_number.strip()
    cleaned_street_name = ' '.join(street_name.strip().title().split())
    print (f"This is {cleaned_name}. {cleaned_name} is {age} years old, and lives at house number {cleaned_house_number} on {cleaned_street_name}.")
except ValueError:
    print("Incorrect number of values entered. Please enter exactly four items separated by commas thank you...")