import turtle, math


# draw a line from (x1, y1) to (x2, y2)
def drawLine(ttl, x1, y1, x2, y2):
    ttl.penup()
    ttl.goto(x1, y1)
    ttl.pendown()
    ttl.goto(x2, y2)
    ttl.penup()

def draw_rail(ttl,x1,y1,x2,y2):
    drawLine(ttl, x1,y1,x2,y2)
    drawLine(ttl, x1,(y1 - 10), x2,(y2 - 10))
    for i in range(x1,x2,40):
        drawPolygon(ttl, i, y2-18,4,6)

def draw_arc(ttl,x,y,h,r,c2):
    turtle.up()
    turtle.goto(x, y)
    turtle.setheading(h)

    turtle.down()
    turtle.circle(r, c2) #  r: radius, c2: 'degree' limit to finish arc


def drawPolygon(ttl, x, y, num_side, radius):
    sideLen = 2 * radius * math.sin(math.pi / num_side)
    angle = 360 / num_side
    ttl.penup()
    ttl.goto(x, y)
    ttl.pendown()
    for iter in range(num_side):
        ttl.forward(sideLen)
        ttl.left(angle)

def drawPolygon_arc_hole(ttl, x, y, num_side, radius):
    sideLen = 2 * radius * math.sin(math.pi / num_side)
    angle = 360 / num_side
    ttl.penup()
    ttl.goto(x, y)
    ttl.pendown()
    for iter in range(num_side):
        if iter == 0 or iter == 2:
            ttl.penup()
            ttl.forward(sideLen)
            ttl.left(angle)
        else:
            ttl.pendown()
            ttl.forward(sideLen)
            ttl.left(angle)

def draw_wheel(ttl,x,y,r1,r2,r3):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color('purple')
    turtle.circle(r1)
    turtle.penup()
    turtle.goto(x, y + r1 -r2)
    turtle.pendown()
    turtle.circle(r2)
    turtle.penup()
    turtle.goto(x, y + r1 - r3)
    turtle.pendown()
    turtle.circle(r3)



def make_wheels_and_rail(ttl):
    draw_rail(ttl, -300, -310, 300, -310)
    draw_wheel(ttl,250,-310,50,40,10)
    draw_wheel(ttl, 110, -310, 50, 40, 10)
    draw_wheel(ttl, -210, -310, 80, 70, 10)
    '''
    for i in range(0,9):
        drawLine(ttl, 250, -260, 250 + 40, -260)
    '''

def make_body(ttl):

##### left most area
    turtle.penup()
    turtle.pendown()
    turtle.begin_fill()
    turtle.color('black')
    # draw the bottom part
    drawPolygon_arc_hole(ttl, -300, -200, 4, 130)
    turtle.end_fill()

    # draw the top part
    turtle.penup()
    turtle.pendown()
    drawPolygon(ttl,-300,-30,4,130)

##### middle body
    # the line in the middle
    turtle.penup()

    turtle.pendown()
    drawLine(ttl,-300,-30,330,-30)
    turtle.penup()

    # upper middle
    turtle.pendown()
    drawLine(ttl,-117,100,330,100)
    drawLine(ttl,330,100,330,-30)

    # lower middle
    # the bottom line, wheel arcs included
    draw_arc(ttl, -117, -200, 90, 92, 180) # big wheel
    draw_arc(ttl, 300, -200, 90, 50, 180) # front wheel

    # drawPolygon_arc_hole(ttl, 200, -200, 4, 75) # frontmost wheel arc
    # drawPolygon_arc_hole(ttl, 60, -200, 4, 75) # middle wheel arc


''' 

def draw_big_arc(ttl):
    turtle.up()
    turtle.goto(-118, -200)
    turtle.setheading(90)

    turtle.down()
    turtle.circle(92, 180)

'''


############################### MAIN

def main():
    # setup screen size
    turtle.setup(800, 800, 0, 0)

    # create a turtle object
    ttl = turtle.Turtle()

    # make the train !! wow!!! choo chooo!!

    make_wheels_and_rail(ttl)
    make_body(ttl)


    # persist drawing
    turtle.done()


main()







