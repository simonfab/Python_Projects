
#
def multiply_or_sum (num1, num2):
   if num1*num2<1000:
    return num1*num2
   else:
    return num1+num2
    

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

print(num1, num2)

result = multiply_or_sum(num1, num2)

print (result)