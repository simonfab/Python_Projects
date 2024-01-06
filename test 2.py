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


# alternative test

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

