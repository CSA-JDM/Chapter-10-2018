# Jacob Meadows
# Computer Programming, 4th Period
# January 22nd, 2018
"""
Create a list called myList with the following six items: 76, 92.3, “hello”, True, 4, 76.
Do it with both append and with concatenation, one item at a time.
Create a list containing 100 random integers between 0 and 1000 (use iteration, append, and the random module).
Write a function called average that will take the list as a parameter and return the average.

ALWAYS USE FUNCTIONS, MAKE THESE SEPARATE FUNCTIONS
"""
import random as rand


def list_review2_1():
    myList = []  # Defining myList as a list
    # Adding all of the requested items into myList through appending and concatenation
    myList.append(76)
    myList.append(92.3)
    myList.append("hello")
    myList.append(True)
    myList.append(4)
    myList.append(76)
    print(myList)
    myList = []
    myList += [76]
    myList += [92.3]
    myList += ["hello"]
    myList += [True]
    myList += [4]
    myList += [76]
    print(myList)


def list_review2_2():
    x = 100  # Wanted range
    list = []  # Defines list that will be of random integers
    for _ in range(x):  # Goes through the wanted range
        list.append(rand.randint(0, 1000))  # Appends the wanted range of random integers of 0 - 1000
    print(average(list))


def average(x):
    b = 0  # Defines variable to use for averaging
    for n in x:  # Goes through all random integers from list
        b += n  # Adds all random integers together
    b = b/len(x)  # Determines the average of all random integers from list
    return b  # Returns average


list_review2_1()
list_review2_2()