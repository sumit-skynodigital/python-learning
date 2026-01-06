#List are built -in data types in Python used to store multiple items in a single variable.
#List items are ordered , changeable, and allow duplicate values.
#List items can be of any data type like string, int, float, bool etc.
#List are indexed, the first item has index [0], the second item has index [1] etc.
#It is also possible to use the list() constructor when creating a new list.
fruits=["apple","mango","cherry"]
print(fruits)
print("Welcome to list module")
print("First item in the list:",fruits[0]) #Accessing the first item in the list
print("Last item in the list:",fruits[-1]) #Accessing the last item in the list
print("Range of items in the list:",fruits[0:2]) #Accessing a range of items in the list
print("Length of the list:",len(fruits))  #Finding the length of the list

#You can change the value of a specific item by referring to its index number
fruits[1]="banana"
print("List after changing the second item:",fruits)
#You can also change a range of item values by referring to a range of index numbers
fruits[0:2]=["kiwi","orange"]
print("List after changing a range of items:",fruits)
#To insert a new item to the list, without replacing any of the existing values, we can use the insert() method.
fruits.insert(1,"grape")
print("List after inserting a new item at index 1:",fruits)
#Append() method will add an item to the end of the list
fruits.append("pear")
print("List after appending a new item:",fruits)

#You can also use the list() constructor to make a list
vegetables=list(("carrot","potato","tomato"))           
print("Vegetable list using list constructor:",vegetables)

#To append elements from another list to the current list, use the extend() method.
#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
tropical_Vegetables=["Pea","Beans","Cucumber"]
vegetables.extend(tropical_Vegetables)
print("Vegetable list after extending with tropical vegetables:",vegetables)

thisTuple=("Pineapple","Watermelon","Papaya")
vegetables.extend(thisTuple)
print("Vegetable list after extending with a tuple:",vegetables) #The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).


#remove() method removes the specified item from the list
fruits.remove("grape")
print("List after removing 'grape':",fruits)   

#pop() method removes the specified index, or the last item if index is not specified
fruits.pop(1)   
print("List after popping the item at index 1:",fruits)
#clear() method empties the list
fruits.clear()
print("List after clearing all items:",fruits)


#Looping through a list
for vegetable in vegetables:    
    print(vegetable)


#list comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
#Example: Create a new list with the names of the Cars in uppercase
cars=["Ford","BMW","Volvo"]
new_cars=[car.upper() for car in cars]          
print("New list with car names in uppercase:",new_cars)

#sort() method sorts the list ascending by default, but you can also make a descending sort, reverse=True
new_cars.sort()
print("New list of cars sorted in ascending order:",new_cars)
new_cars.sort(reverse=True)
print("New list of cars sorted in descending order:",new_cars)

#reverse() method reverses the order of the list
new_cars.reverse()
print("New list of cars after reversing the order:",new_cars)

#copy() method returns a copy of the list
new_cars_copy=new_cars.copy()
print("Copy of the new cars list:",new_cars_copy)


#join list items using extend() method
bikes=["Yamaha","Honda","Suzuki"]
cars.extend(bikes)      
print("Cars list after extending with bikes list:",cars)

#join list items using + operator
all_vehicles=cars+bikes     
print("All vehicles list by joining cars and bikes using + operator:",all_vehicles) 

#join list items using append() method in a loop
all_vehicles_loop=[]
for vehicle in cars:
    all_vehicles_loop.append(vehicle)
for vehicle in bikes:
    all_vehicles_loop.append(vehicle)
print("All vehicles list by joining cars and bikes using append() method in a loop:",all_vehicles_loop)