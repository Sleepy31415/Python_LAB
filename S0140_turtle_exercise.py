"""
Exercise "Tom the Turtle":

As always, read the whole exercise description carefully before you begin to solve the exercise.

Copy this file into your own solution directory. Write your solution into the copy.

The function "demo" introduces you to all commands you need to interact with Tom in the following exercises.

Only if you are curious and love details:
    Here is the full turtle graphics documentation:
    https://docs.python.org/3.3/library/turtle.html

Part 1:
    Write a function "square" which accepts a parameter "length".
    Calling this function causes the turtle to draw a square with a side length of "length" pixels.

Part 2:
     Complete the function "visible" which shall return a boolean value,
     indicating if the turtle is in the visible area of the screen.
     Use this function in the following parts of this exercise
     to return the turtle to the screen when it wandered off.

Part 3:
    Write a function "many_squares" with a for loop, which calls square repeatedly.
    Use this function to draw several squares of different sizes in different positions.
    The function shall have some parameters. For example:
        number: how many squares will be drawn?
        size: how large are the squares?
        distance: how far away from the last square is the next square positioned?

Part 4:
    Write a function that produces patterns similar to this:
    https://pixabay.com/vectors/spiral-square-pattern-black-white-154465/

Part 5:
    Write a function that produces patterns similar to this:
    https://www.101computing.net/2d-shapes-using-python-turtle/star-polygons/
    The function shall have a parameter, that influences the shape of the pattern.

Part 6:
    Create your own function that produces a cool pattern.
    Later, if you like, present your pattern on the big screen to the others.

When your program is complete, push it to your github repository.
Then send this Teams message to your teacher: <filename> done
Thereafter go on with the next file.
"""

import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.
import random as rd


# from random import random

# checks if turtle is visible on the screen and returns it to the middle if wandered_off = True
def visible(turtle_name):  # returns true if both the x- and y-value of the turtle's position are between -480 and 480
    wandered_off = False

    while (turtle.done != True):
        if (turtle_name.position()[0] > 480 or turtle_name.position()[0] < -480 & turtle_name.position()[1] > 480 or turtle_name.position()[1] < -480):
            wandered_off = True
            turtle_name.home()

        else:
            wandered_off = False
    return 0


# demo drawing
# def demo():  # demonstration of basic turtle commands
#     tom = turtle.Turtle()  # create an object named tom of type Turtle
#     print(type(tom))
#     tom.speed(5)  # fastest: 10, slowest: 1
#     for x in range(8):  # do the following for x = 0, 1, 2, 3, 4, 5, 6, 7
#         tom.forward(50)  # move 50 pixels
#         tom.left(45)  # turn 45 degrees left
#         print(f'Tom is now at {tom.position()}, x-value: {tom.position()[0]=:.2f}, y-value: {tom.position()[1]=:.2f}')
#     tom.penup()  # do not draw while moving from now on
#     tom.forward(100)
#     tom.pendown()  # draw while moving from now on
#     tom.pencolor("red")  # draw in red
#     tom.right(90)  # turn 90 degrees right
#     tom.forward(120)
#     tom.right(-90)  # turning -90 degrees right is the same as turning +90 degrees left
#     tom.forward(120)
#     tom.home()  # return to the original position in the middle of the window
#     turtle.done()  # keeps the turtle window open after the program is done
#
#
# demo()


# something I will need
# x-value: turtle_name.position()[0]
# y-value: turtle_name.position()[1]


# square made with turtle named steve
# def square():
#     length = 100
#     steve = turtle.Turtle()
#     print(type(steve))
#     #i´m using range so that you can make multiple squares of the same size, if you comment out turtle.done()
#     steve.speed(1)
#     for x in range(1):
#         steve.right(90)
#         steve.forward(length)
#         steve.right(90)
#         steve.forward(length)
#         steve.pencolor("magenta")
#         steve.right(90)
#         steve.forward(length)
#         steve.right(90)
#         steve.forward(length)
#
#         turtle.done()
#
#
# square()

# square randomizer



# square function for many_squares
# def make_squares():
#
#     x = 0
#     square_amount = rd.randrange(2, 5)
#     square_size = rd.randrange(25, 50)
#     square_distance = rd.randrange(10, 25)
#     robert = turtle.Turtle()
#
#     while x < square_amount:
#         robert.penup()
#         robert.forward(square_distance)
#         robert.pendown()
#         robert.right(90)
#         robert.forward(square_size)
#         robert.right(90)
#         robert.forward(square_size)
#         robert.pencolor("green")
#         robert.right(90)
#         robert.forward(square_size)
#         robert.right(90)
#         robert.forward(square_size)
#         # turtle.done()
#         x += 1

def for_loop_solution(): # this is the exact same code (aside from dumb_solution_while_amount=rd.randrange(2, 7) ) that is shown above, but with a for loop added because the assingment required it.
    dumb_solution_while_amount=rd.randrange(2, 7)
    square_amount = {rd.randrange(2, 8)}
    square_size = rd.randrange(25, 50)
    square_distance = rd.randrange(10, 25)
    robert = turtle.Turtle()
    x=0
    for int in square_amount:
        while x < dumb_solution_while_amount:
            robert.penup()
            robert.forward(square_distance)
            robert.pendown()
            robert.right(90)
            robert.forward(square_size)
            robert.right(90)
            robert.forward(square_size)
            robert.pencolor("green")
            robert.right(90)
            robert.forward(square_size)
            robert.right(90)
            robert.forward(square_size)
            # turtle.done()
            x += 1


#function for creating a spiral similar to: https://pixabay.com/vectors/spiral-square-pattern-black-white-154465/

def make_spiral():

    michelle = turtle.Turtle()
    print(type(michelle))
    michelle.speed(1)
    for x in range(1):
        michelle.penup()
        michelle.goto(-370, 315)
        michelle.pendown()
        michelle.forward(730)
        michelle.right(90)
        michelle.forward(615)
        # michelle.pencolor("magenta")
        # michelle.right(90)
        # michelle.forward(length)
        # michelle.right(90)
        # michelle.forward(length)

        turtle.done()


# make_squares()
make_spiral()

