"""
Exercise "The inventory sequence"

As always, read the whole exercise description carefully before you begin to solve the exercise.

This exercise is an optional challenge for the excellent programmers among you.
You absolutely do not have to solve this exercise in order to proceed successfully.

Copy this file into your own solution directory. Write your solution into the copy.

Watch the first 3 minutes of this video:
https://www.youtube.com/watch?v=rBU9E-ZOZAI

Write a function "inventory" which produces the numbers shown in the video.
The function accepts a parameter defining how many number rows to produce.
The function prints out the numbers of each row.

You will probably want to define a function count_number which counts how often a certain number
appears in the current number sequence.

In the main program, call inventory with 6 as an argument.

If you have no idea how to begin, have a look at the solution in S1720_inventory_solution.py

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""


def inventory(n, rows):
    strings = n.split(" ")  # split start into a list of strings
    number = []  # numbers is a list and will later contain numbers
    for s in strings:
        if len(s) > 0:
            number.append(int(s.strip()))  # strip removes white spaces and similar characters from the beginning and end of string1
    list_of_lists = [number]  # number_lists is a list and will later contain lists of numbers
    index_shift = 0
    for i in range(rows):
        while n != 0:
            list_of_lists[i].insert(i + 1 + index_shift, list_of_lists.count(n))
            i += 1
            index_shift +=1
        list_of_lists[i].insert(i + 1 + index_shift, list_of_lists.count(n))
        print(list_of_lists, end="")








# while loop is not working


#first try
# numbers = [n]
# # string = input("write a whole number: ")
# # for s in string:
# #     if len(s) > 0:
# #         numbers.append(int(s.strip()))  # strip removes white spaces and similar characters from the beginning and end of string1
# # n = numbers[0]
# list_of_lists = [numbers]
# # need to double-check the i+1 amounts. I might need index_shift
# index_shift = 0
# for i in range(rows):
#     while n != 0:
#         list_of_lists[i].append(i + index_shift, list_of_lists[i].count(n))  # unsure of this line
#         index_shift += 1
#     list_of_lists[n].append(i + 1, list_of_lists[i + 1].count(n))  # not sure about index shift. [i] might be lazy

number_input=input("enter the number to start with: ")
rows_input = int(input("Enter the number of rows to print: "))
inventory(number_input, rows_input)