""" greeting = "Hello!"
print (greeting[1:2]) """

""" 
number_builder = []
i=1
while i <=50:
    if i %2 == 0:
        print (i)
        number_builder.append(str(i))
    i +=1
print (" ".join(number_builder)) """


""" # alternative test

user_string = input("Please enter your string..\n")
new_string = ""
for i in range (len(user_string)):
    if i %2 == 0:
        new_string += user_string[i].upper()
    else:
        new_string += user_string[i].lower()
print (new_string)


#new_string = new_string.lower()
new_string_list = new_string.split()
print(new_string_list)
for i in range (len(new_string_list)):
    if i %2 == 1:
        new_string_list[i] = new_string_list[i].upper()
    else:
        new_string_list[i] = new_string_list[i].lower()
new_string = str(" ".join(new_string_list))
    # print (f"{new_string_list[i]}\n")
print (new_string)
 """


''' a = [1,2,3]
b = ["smile", "frown", "snarl"]
string_list = ["dog","cat","rat"]
my_nested_list = [a,b,string_list, "human"]
print (my_nested_list)

b2 = b.pop(1)
print (b)
print (my_nested_list)

print (string_list)

text = string_list.pop(1)
print(text)
print (string_list)'''

""" a = [1,2,3]
b = a.copy()
print (a)
print (b)
a[1] = 7
print (a)
print (b) """

""" num_list = [1,2,3,4,5,6,7,8,9,10,11,12]
print (num_list)
a = int(num_list[0])+num_list[1]
print(a)
multiplyedby3 = [int(num) *3 for num in num_list]
print (multiplyedby3) """

stock_value = 0
menu = ("Tea", "Coffee", "Sandwich", "Cake")
stock_qty = {"Tea": 100,
         "Coffee": 200,
         "Sandwich": 30,
         "Cake": 25}
cost_price = {"Tea": 2.5,
         "Coffee": 3.0,
         "Sandwich": 2.10,
         "Cake": 3.25}
print()
for item in menu:
    stock_value += stock_qty[item]*cost_price[item]
    print (f"{item} = {stock_qty[item]} on hand at £{cost_price[item]} each = "
           f"{stock_qty[item]*cost_price[item]}")
print(f"\nTotal stock value = £{stock_value}")

