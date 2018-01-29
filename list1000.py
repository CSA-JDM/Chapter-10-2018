# Jacob Meadows
# Computer Programming, 4th Period
# January 24th, 2018
"""
Create a list with 5 names
Create a function that asks the user for a name, then adds that to the existing list (PASS THAT FIRST LIST TO THIS FUNCTION, THEN RETURN THE NEW LIST!)
Print the new list

Only thing I care about are using functions, and using PASS AND RETURNING OF VALUES!
"""
list1 = ["Billy", "Michael", "Joseph", "Angelica", "Moreish"]


def list1000():
    global list1
    list1 = askname(list1)
    again(list1)

def askname(x):
    y = input("New Name: ")
    x.append(y)
    return x


def again(l):
    x = input("Would you like to add another new name? (1. Yes or 2. No): ")
    if x.lower() == "yes" or x.lower() == "1":
        list1000()
    elif x.lower() == "no" or x.lower() == "2":
        print(l)
    else:
        print("Please input one of the given choices.")
        again(l)


list1000()
