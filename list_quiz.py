# Jacob Meadows
# Computer Programming, 4th Period
# January 11th, 2018
"""
list_quiz.py
names=Create a list with 5 names
numbers=Create another list with 5 double digit numbers
both=Create a list that puts these two lists into one
squeezed=Squeeze 2 new names into the list of names (don't care where, but not at the beginning or end) <--- this shows me you understand the 'squeeze' process

Print all the lists
"""


def list_quiz():
    name = ["Jimmy", "Michael", "Francis", "Bartheole", "Tony"]
    numbers = [10, 11, 12, 13, 14]
    both = name[:] + numbers[:]
    squeezed = name[:]
    squeezed[3:3] = ["Yunolo", "Xenoth"]
    print(name, numbers, both, squeezed)


list_quiz()