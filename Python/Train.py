import turtle, math

################## Functions

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
    turtle.penup()

def draw_arc(ttl,x,y,h,r,c2):
    turtle.up()
    turtle.goto(x, y)
    turtle.setheading(h)

    turtle.down()
    turtle.circle(r, c2) #  r: radius, c2: 'degree' limit to finish arc


def draw_dots(ttl, length, h ):
    turtle.pendown()
    turtle.setheading(h) 
    for i in range (length//10):
        turtle.pendown()
        turtle.dot()
        turtle.penup()
        turtle.forward(10)
        #i += 10


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
    inc = turtle.Turtle()
    inc.speed(0)
    inc.penup()
    inc.goto(x, y + r1 - r2)
    inc.color('red')

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color('red')
    turtle.circle(r1)
    turtle.penup()
    turtle.goto(x, y + r1 -r2)
    turtle.pendown()
    turtle.circle(r2)
    turtle.penup()
    turtle.goto(x, y + r1 - r3)
    turtle.pendown()
    turtle.circle(r3)

    turtle.penup()

    spoke_angle = 5
    for r in range(2):
        for q in range(9):
            turtle.penup()
            inc.goto(x, y + r1 - r2)
            inc.pendown()
            inc.circle(r2, q * 45)

            ttl.goto(x, y + r2)
            ttl.pendown()
            ttl.circle(r1 - r2, spoke_angle)
            ttl.goto(inc.position())

            inc.penup()
            ttl.penup()
            spoke_angle += 45
            inc.setheading(0)
            ttl.setheading(0)
        spoke_angle = -10

    inc.ht()
    ttl.ht()

def make_wheels_and_rail(ttl):
    draw_rail(ttl, -300, -310, 300, -310)
    draw_wheel(ttl,250,-310,50,40,10)
    draw_wheel(ttl, 110, -310, 50, 40, 10)
    draw_wheel(ttl, -210, -310, 80, 70, 10)


#################### make train body
def make_body(ttl):


##### left most area
    turtle.penup()
    turtle.pendown()
    turtle.begin_fill()
    turtle.color('black', 'orange')
    # draw the bottom part
    drawPolygon_arc_hole(ttl, -300, -200, 4, 130)
    turtle.end_fill()

    # top rectangle section
    turtle.penup()
    turtle.pendown()
    drawPolygon(ttl,-300,-30,4,130)

    # skinny rectangle on top of other rectangle
    drawLine(ttl, -315,155,-105,155)
    drawLine(ttl, -315,165,-105,165)
    drawLine(ttl, -315,165,-315,155)
    drawLine(ttl, -105,165,-105,155)

    turtle.penup()


    # draw windows
    turtle.penup()
    turtle.setheading(45)
    turtle.goto(-230, 60)
    turtle.pendown()
    turtle.begin_fill() # yellow filled windows lol
    turtle.color('yellow')
    turtle.circle(40, steps=4) # window 1
    turtle.penup()
    turtle.goto(-130, 60)
    turtle.pendown()
    turtle.circle(40, steps=4) # window 2
    turtle.end_fill()
    turtle.penup()
    turtle.color('black')


##### middle body
    # the line in the middle
    turtle.penup()
    turtle.pendown()
    drawLine(ttl,-115,-30,330,-30)
    drawLine(ttl,-115,-40,330,-40)
    turtle.penup()
    turtle.goto(-100,-35)
    turtle.pendown()
    draw_dots(ttl,440, 0)
    turtle.pensize(1)
    turtle.penup()


    # upper middle
    turtle.pendown()
    drawLine(ttl,-117,100,330,100)
    drawLine(ttl,330,100,330,-30)

    # left vertical double line (rect)
    drawLine(ttl,8,100,8,-30)
    drawLine(ttl,-2,100,-2,-30)
    turtle.penup()
    turtle.goto(4,95)
    turtle.pendown()
    draw_dots(ttl,130, 270) # length 70 since vertical, h = 270 since going down

    # right vertical double line (rect)
    drawLine(ttl, 54, 100, 54, -30)
    drawLine(ttl, 64, 100, 64, -30)
    turtle.penup()
    turtle.goto(59, 95)
    turtle.pendown()
    draw_dots(ttl, 130, 270)

    # double vertical line (smoke)
    drawLine(ttl, 140, 100, 140, -30)
    drawLine(ttl, 150, 100, 150, -30)
    turtle.penup()
    turtle.goto(145, 95)
    turtle.pendown()
    draw_dots(ttl, 130, 270)

    # lower middle

    # the bottom line, wheel arcs included
    draw_arc(ttl, -117, -200, 90, 92, 180) # big wheel
    draw_arc(ttl, 300, -200, 90, 50, 180) # front wheel
    draw_arc(ttl, 160, -200, 90, 50, 180) # middle wheel
    drawLine(ttl, -117,-200,60,-200) # big to middle line
    drawLine(ttl, 160,-200,200,-200) # middle to front wheel
    drawLine(ttl, 300,-200,330,-200) # front wheel to lower train
    drawLine(ttl, 330,-240,330,-30) #lower train to upper middle
    
    

    # drawPolygon_arc_hole(ttl, 200, -200, 4, 75) # frontmost wheel arc
    # drawPolygon_arc_hole(ttl, 60, -200, 4, 75) # middle wheel arc
    turtle.penup()


##### front
    turtle.pendown()

    # fat block
    drawLine(ttl,355,85,355,-15)
    drawLine(ttl,330,85,355,85)
    drawLine(ttl,330,-15,355,-15)

    # skinny block
    drawLine(ttl,368,55,368,15) # vertical
    drawLine(ttl,355,55,368,55) # H
    drawLine(ttl,355,15,368,15) # H

    # front guard trapezoid thing
    drawLine(ttl,330,-240,395,-240)
    drawLine(ttl,330,-130,350,-130)
    drawLine(ttl,350,-130,395,-240)


##### top of  train
    # the rectangles
    turtle.color('blue')
    drawLine(ttl, 10,120,50,120)
    drawLine(ttl, 10,120,10,100)
    drawLine(ttl, 50,120,50,100)
    drawLine(ttl, 20,125,40,125)
    drawLine(ttl, 20,125,20,120)
    drawLine(ttl, 40,125,40,120)

    # smoke chimney
    drawLine(ttl, 115,160,175,160)
    drawLine(ttl, 115,160,130,100)
    drawLine(ttl, 175,160,160,100)
    drawLine(ttl, 175,160,160,175)
    drawLine(ttl, 115,160,130,175)
    drawLine(ttl, 160,175,130,175)


    # initial smoke cloud coordinates
    turtle.penup()
    turtle.pensize(5)
    turtle.color('black')
    s_x = 115
    s_y = 240
    turtle.fillcolor('black')
    # actual smoke clouds
    for iter in range (4):
        turtle.penup()
        turtle.goto(s_x, s_y)
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(30)
        turtle.end_fill()
        s_x += 55
        s_y += 45


    turtle.end_fill()

############################### MAIN ############################

def main():
    # setup screen size
    turtle.setup(800, 800, 0, 0)


    # create a turtle object
    ttl = turtle.Turtle()

    # make the train !! wow!!! choo chooo!!
    make_wheels_and_rail(ttl)
    make_body(ttl)

    # hide turtle
    turtle.hideturtle()
    # persist drawing
    turtle.done()

main()







