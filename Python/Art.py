#  File: Art.py

#  Description: This assignment creates circles within circles using recursion

#  Student Name: Rohan Chaudhry

#  Student UT EID: rc43755

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created: Feb 26

#  Date Last Modified: Mar 1

####################################################################3
import os # add per Ridwan's instruction
import turtle, random


def drawCircle(ttl, radius, counter):

    if radius > 5:
        counter = radius*(3/200) - .0125
        ttl.pensize(counter) # circle thickness thins as it nears the center
        ttl.penup()

        ttl.color(randcolor()) # circle is random color
        ttl.goto(0, -radius)  # go to the very bottom of the screen
        ttl.pendown()

        ttl.circle(radius)

        # draw thin triangles
        ttl.pensize(0)
        ttl.penup()
        ttl.color('black')
        ttl.goto(0, -radius)
        ttl.pendown()
        ttl.circle(radius, steps=3)
        ttl.penup()

        # recursion
        drawCircle(ttl, radius/2, counter)


def tri_lines(ttl,lines, radius): # draw a line from the center, through each triangle vertex
    if lines > 0:
        ttl.penup()
        ttl.goto(0, 0)
        ttl.pensize(1)
        ttl.color('black')
        ttl.pendown()
        ttl.forward(radius)
        ttl.penup()
        ttl.backward(radius)
        ttl.left(120)
        tri_lines(ttl, lines - 1, radius)


def randcolor(): # randomly sort the list of colors and return the first color
    colors = ["blue","brown","red","green","orange","turquoise","pink"]
    random.shuffle(colors)
    return colors[0]


def main():

    print("Recursive Art\n")
    radius = eval(input("Enter a level of recursion between 1 and 6: "))
    while (radius < 1 or radius > 6): # check input
        radius = eval(input("enter circle radius between 1 and 6: "))

    turtle.tracer(10000)  # add per Ridwan's instruction

    # setup screen size and initialize turtle
    turtle.setup(800, 800,0,0)
    ttl = turtle.Turtle()

    # scale the circle to fit the screen
    # enter 6 = radius of 400
    radius = radius*(200/3)
    counter = radius
    lines = 3

    # draw and persist
    drawCircle(ttl, radius, counter)
    ttl.setheading(30)
    tri_lines(ttl,lines, radius)
    ttl.hideturtle()
    #turtle.done() # delete per Ridwan's instruction


    # add per Ridwan's instruction
    outName = os.path.basename(__file__)[:-2] + 'eps'
    turtScrn = turtle.getscreen()
    turtScrn.getcanvas().postscript(file=outName)


main()