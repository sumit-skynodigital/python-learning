# Conditions in Python are used to perform different actions based on different conditions.
#Python supports the usual logical conditions from mathematics: equals: a == b
#not equals: a != b 
#greater than: a > b
#less than: a < b
#greater than or equal to: a >= b
#less than or equal to: a <= b
a=33
b=200   
if b > a:
    print("b is greater than a")
#The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition"
elif a == b:
    print("a and b are equal")      
#The else keyword catches anything which isn't caught by the preceding conditions
else:
    print("a is greater than b")
    
#checking number is potoive, negative or zero
num=int(input("Enter a number: "))
if num > 0: 
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")    


#nested if
x = int(input("Enter a number: "))
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
#The pass statement is used when a statement is required syntactically but you do not want any command or code to execute.
#In Python, if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
y = 5
if y > 2:
    pass

#and, or not
a = 200             
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")
if a > b or a > c:
    print("At least one of the conditions is True")
if not a > b:
    print("a is NOT greater than b")

#nested if with and, or
x = 15
if x > 10:
    if x < 20:
        print("x is between 10 and 20")
if x > 5 and x < 25:

    print("x is between 5 and 25")
if x < 10 or x > 20:
    print("x is either less than 10 or greater than 20")

#ternary operator
age = 15
status = "teenager" if age < 18 else "adult"
print(status)
#Output: teenager


#match statement 
day = "Monday"
match day:
    case "Monday":
        print("Start of the work week")
    case "Wednesday":
        print("Midweek day")
    case "Friday":
        print("End of the work week")
    case _:   #default case, Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches:
        print("Just another day")