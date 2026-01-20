#Python for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
cars = ["BMW", "VW", "FORD"]

for car in cars:
    for letter in car:
        print(letter)
    #if car != cars[-1]: #To avoid printing "-----" after the last car 
    print("-----")	

#Using the break statement to stop the loop before it has looped through all the items
for car in cars:
    print(car)
    if car == "VW":
        break
    print("This will not be printed for VW and cars after it.")

#Using the continue statement to skip the current iteration of the loop
for car in cars:
    if car == "VW":
        continue
    print(car)
    print("This will not be printed for VW but will be printed for other cars.")

#Using the range() function to loop through a set of code a specified number of times, range(start, stop) → starts at start, stops before stop.
for i in range(1, 6):
    print("range:", i)
#Using range() with a step parameter range(start, stop, step)
for i in range(0, 11, 2):  #Even numbers from
    print("Range using step:", i)

#Nested for loop
for i in range(1, 3):  #Outer loop
    print("Outer loop iteration:", i)
    for j in range(1, 4):  #Inner loop
        print("  Inner  iteration:", j)
       