'''Task 12 - Cafe stock valuation using list and dictionaries

Student details:
#student_name = "Simon Kinsey" 
#student_number = "SK23110011962"

Notes:
pylint line length limit followed (100 chars)
note to self - research "enumerate" as this gives an automatic counter
    - does this work with dict loops?

Pseudo code:
set up variable for stock value
set up list of stock items - call it "menu"!
set up dictionary for current stock qty holding - call it "stock_qty"
set up dictionary for cost prices of stock items - call it "cost-_price"
loop through all the items and
    add value of line stock holding to current stock value as a cumulative
    print line value
print a blank line
print total stock holidng value
'''

# initialise variables
stock_value = 0

# set up list of stock items - call it menu
menu = ("Tea", "Coffee", "Sandwich", "Cake")

# set up dict to store current stock qty of menu items
stock_qty = {"Tea": 100,
         "Coffee": 200,
         "Sandwich": 30,
         "Cake": 25}

# set up dict to store ccost price of menu items
cost_price = {"Tea": 2.5,
         "Coffee": 3.0,
         "Sandwich": 2.10,
         "Cake": 3.25}

# print a blank line
print()

# loop though the items in the menu list
# calulate line value
# add line value to stock total value
# print line valuation

for item in menu:
    item_value = stock_qty[item] * cost_price[item]
    stock_value += item_value
    print (f"{item} = {stock_qty[item]} on hand at £{cost_price[item]} each = "
           f"£{item_value}")

# print total value
print(f"\nTotal stock value = £{stock_value}")
