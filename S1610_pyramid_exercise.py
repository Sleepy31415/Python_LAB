"""
Exercise "Number pyramid":

As always, read the whole exercise description carefully before you begin to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.

Watch the first 93 seconds of this video: https://www.youtube.com/watch?v=NsjsLwYRW8o

Write a function "pyramid" which produces the numbers shown in the video.
The function has a parameter defining how many number rows to produce.
The function prints out the numbers of each row and also their sum.

In the main program, call the function with 1, 2, 3, ..., 10 as an argument.

Add a more general function pyramid2.
This function has as a second parameter a list with the numbers of
the pyramid's topmost row.

In the main program, call pyramid2 with 1, 2, 3, ..., 10 as the first argument
and a list of numbers of your choice as the second argument.
Try out different lists as the second argument.

If you have no idea how to begin, open S1620_pyramid_help.py and start from there

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""

def make_list_of_lists():
    i = 0
    input_number = input("write a number: ")
    input_number = int(input_number)
    print(input_number)
    list = [input_number,input_number]
    list_of_lists =[list]
    print(list_of_lists)
    return input_number


# def pyramid():
#     new_changed_number = make_list_of_lists.input_number + 1
#     i = 0
#     for item in range(1,input_number + 1)
#         if list_of_lists[i][0] + 1 == list_of_lists[i][1] + 1:
#             list_of_list[i+1].expand( 1, list_of_lists[i][1])
#
#
#

# first code
# new_changed_number = make_lists().input_number + 1
# i = 0
# for item in range(1, 2):
#     if list[i] + 1 == list[1] + 1:
#         list.insert(i + 1, new_changed_number)
#         print(list)
#         new_changed_number += 1
#         i += 1

#make a list of list code
#def make_lists():
#     print("skriv et tal")
#     input_number = input()
#     list = [input_number, input_number]
#     list_of_lists = [list]
#     return input_number

