# Jacob Meadows
# Computer Programming, 4th Period
# January 17th, 2018
"""
Program should be list2.py
Create a list that has your name, birthday (separate day, month, and year), and place of birth
Using a fit loop print the whole list
Using index references print "I was born in (place)"
Using index references print "The month was (month)"
Add parent's name
Print new list
Read the rest of chapter 10
"""


def list2():
    list = ["Jacob", "April", "10th", "2002", "Connecticut"]
    for x in range(len(list)):
        print(list[x])
    for x in range(len(list)):
        if x == 0:
            print("My name is %s." % list[x])
        elif x == 4:
            print("I was born in %s." % list[x])
        elif x == 1:
            print("The month was %s." % list[x])
        elif x == 2:
            print("It was the %s day." % list[x])
        elif x == 3:
            print("The year was %s." % list[x])
    list[1:1] = ["Saodah"]
    print(list)


list2()
