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
    
#slicing can also be done with the strings both positive and negative, and the strating index is [0]
print(txt[0:20])
print(txt[-18:-1])
print(txt.upper())  #This will convert the string to upper case
print(txt.lower())   #This will convert the string to lower case
print(txt.strip())   #This will remove any whitespace from the beginning or the end
print(txt.replace("mind","soul"))  #This will replace the word mind with soul
print(txt.split(" "))   #This will split the string into a list



#String concatenation
x="Welcome"
y="to string module"    
z=x+y
w=x+" "+y  #adding a space between two strings
print(z)    
print(w)


#Better way to concatenate strings is using f-strings() method
age=25
text=f"my name is John, and I am {age}"
print(text)