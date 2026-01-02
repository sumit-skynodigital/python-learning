"""
Strings in python are surrounded by either single quotation marks, or double quotation marks.
You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
"""

print("Welcome to string module")
print("Welcome to string 'MODULE'")
print('Welcome to string "MODULE"')

#You can assign a multiline string to a variable by using three quotes:or using single three quotes
a="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua"""
print(a)



"""Like many other popular programming languages, strings in Python are arrays of unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string."""

b="String is a array"
print(b[0:15])
print("Lenght of string:",len(b))       #len is used to find the length of a string
print("Verify the content in the string is present:","is" in b)  #This will check the content in the string and return the bool response
#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
print("Using 'not in' to check phrase or char is NOT present in string:","PRESENT" not in b)

#You can also check this using the if statement
txt="Aparts form Thought there is no such thing as mind"
if "Travel" not in txt:
    print("No, 'Travel' is not present")

#Looping through the string: and below eaxmple will print output like 
for c in "banana":
    print(c)
    




