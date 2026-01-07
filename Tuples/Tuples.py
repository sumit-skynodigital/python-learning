"""Tuples are used to store multiple items in a single variable.
Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
A tuple is a collection which is ordered and unchangeable.
Tuples are written with round brackets."""

thisTuple=("apple","banana","cherry")
print(thisTuple)
print("Welcome to tuple module")
print("First item in the tuple:",thisTuple[0]) #Accessing the first item in the tuple
print("Last item in the tuple:",thisTuple[-1]) #Accessing the last item in the tuple
print("Range of items in the tuple:",thisTuple[0:2]) #Accessing a range of items in the tuple
print("Length of the tuple:",len(thisTuple))  #Finding the length of the tuple  



#Tuples are unchangeable, meaning that we cannot change, add, or remove items after the tuple has been created.
#But we can convert the tuple into a list, make the changes, and convert it back into a tuple.
#Convert the tuple into a list to be able to change it or remove items
thisList=list(thisTuple)
thisList[1]="orange"  #Changing the second item
thisTuple=tuple(thisList)  #Convert the list back into a tuple
print("Tuple after changing the second item:",thisTuple)


#Create tuples with one item
thisTuple1=("apple",)  #Note the comma after the item   
print("Tuple with one item:",thisTuple1)
#Without the comma, Python will not recognize it as a tuple
thisTuple2=("banana")  #This is not a tuple
print("Type of thisTuple2 (without comma):",type(thisTuple2))

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[::-1][:3])  #Reverse the tuple and get the first three items

#adding tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print("Concatenated tuple:",tuple3)
#The del keyword can delete the tuple completely
del tuple3
#print(tuple3) #This will raise an error because the tuple no longer exists 


#unpacking a tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print("Green fruit:",green)
print("Yellow fruit:",yellow)
print("Red fruit:",red)
#Using Asterisk* when unpacking a tuple
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print("Green fruit:",green)
print("Yellow fruit:",yellow)
print("Red fruits:",red)  #red will be a list containing the remaining items

#if German has asterisk*
cars=("BMW","VW","TOYOTA","BYD")
(*German, Japanese, Chinese)=cars #Unpacking with asterisk*
print("German cars:",German) #german will be a list containing the first two items
print("Japanese cars:",Japanese)
print("Chinese cars:",Chinese)

#mutiple of tuples
bikes=("ZX10R","Z-900","H2R")
myTuple=bikes*2
print("My bikes tuple:",myTuple)