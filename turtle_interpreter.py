import turtle


class TurtleInterpreter:
    '''Initializes TurtleInterpreter class with a turtle setup and tracer'''
    def __init__(self, dx = 800, dy = 800):
        turtle.setup(dx, dy)
        turtle.tracer(False)
       


    def drawString(self, dstring, distance, angle):
        """ Interpret the characters in string dstring as a series
    of turtle commands. Distance specifies the distance
    to travel for each forward command. Angle specifies the
    angle (in degrees) for each right or left command. The list   
    of turtle supported turtle commands is:
    F : forward
    - : turn right
    + : turn left
    [ : save the turtle's heading and position
    ] : restore the turtle's heading and position
    '<': pushes the current turtle color onto a color stack
    '>': pops the current turtle color off the color stack and set the turtle's color to that value
    'g': sets the turtle's color to green
    'y': sets the turtle's color to light yellow
    'r': sets the turtle's color to light red
    """
        stack = []
        colorstack = []
        for char in dstring:
            if char == 'F':
                turtle.forward(distance)
            elif char == '-':
                turtle.right(angle)
            elif char == '+':
                turtle.left(angle)
            elif char == '[':
                stack.append(turtle.position())
                stack.append(turtle.heading())
            elif char == ']':
                turtle.penup()
                turtle.setheading(stack.pop())
                turtle.goto(stack.pop())
                turtle.pendown()
            elif char == '<':
                colorstack.append(turtle.color()[0])
            elif char == '>':
                colorstack.pop()
            elif char == 'g':
                turtle.color(0.15, 0.5, 0.2)
            elif char == 'y':
                turtle.color(0.8, 0.8, 0.3)
            elif char == 'r':
                turtle.color(0.7, 0.2, 0.3)
        turtle.update()
        

    def hold(self):
        '''Holds the screen open until user clicks or presses 'q' 
        key'''

        # Hide the turtle cursor and update the screen
        turtle.hideturtle()
        turtle.update()

        # Close the window when users presses the 'q' key
        turtle.onkey(turtle.bye, 'q')

        # Listen for the q button press event
        turtle.listen()

        # Have the turtle listen for a click
        turtle.exitonclick()


    def place(self, xpos, ypos, angle = None):
        '''positions the turtle pointer at a specified position (xpos,ypos) on the turtle screen and sets its head it according to the specified angle'''
        turtle.penup()
        turtle.goto(xpos,ypos)
        if angle != None:
            turtle.setheading(angle)
        turtle.pendown


    def orient(self, angle):
        '''orients the turtle pointer according to the angle given'''
        turtle.setheading(angle)
    

    def goto(self, xpos, ypos):
        '''positions the turtle pointer at a specified position (xpos,ypos) on the turtle screen'''
        turtle.up()
        turtle.goto(xpos, ypos)
        turtle.down()


    def setColor(self, c):
        '''gives a specific colour to the turtle drawing'''
        turtle.color(c)


    def setWidth(self, w):
        '''sets the width of the turtle drawing'''
        turtle.width(w)




    
