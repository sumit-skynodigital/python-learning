"""Python Loops
Python has two primitive loop commands:
while loops
for loops"""
#while loop
i = 1
while i < 6:
    print(i)
    i += 1
#Output: 1 2 3 4 5

#break statement
i = 1
while i < 6:
    print(i,"Break Test")
    if i == 3:
        break
    i += 1
#Output: 1 2 3
#continue statement
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i,"Continue Test ")
#Output: 1 2 4 5 6


a=0
while a<=10:
    if a % 2 ==0:
        print(a,"is even")
    else:
        print(a,"is odd")
    a += 1
#Output: 0 is even 1 is odd 2 is even 3 is odd...