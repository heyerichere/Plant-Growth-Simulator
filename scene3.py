'''scene3.py
12/10/2022
CS151 F22  Final project
Eric Appiah'''


import random
import turtle_interpreter
import lsystem
import turtle


def main():
    '''
    Test the ability of the TurtleInterpreter to draw trees.
    The program receives the name of an L-system file and
    draws three trees on the screen, using 10 iterations respectively
    of the rule to generate the string.
    If the TurtleInterpreter draws leaves using the L symbol, then
    the program also draws piles of leaves at the base of each tree.
    '''

    tree = []

    sx = 800
    sy = 450
    terp = turtle_interpreter.TurtleInterpreter(sx, sy)
    N = 10

    for j in range(N):
        tree.append(lsystem.Lsystem('systemA1.txt'))

    for i in range( N ):
        x0 = -sx/3 + i*0.75*sx/(N+1) +  -sx//(3*N) + (20*i)
        y0 = -sy/4 +  -sy//20 + (60*i)

        tstr = tree[i].buildString(3+i)

        terp.setColor( (0.5, 0.4, 0.3 ) )
        terp.place( x0, y0, random.randint( 85, 95 ) )
        turtle.color(0.15, 0.5, 0.2)
        for i in range(40):
            terp.drawString( tstr, random.randint( 2, 4 ) , random.randint( 18, 30 ) * random.choice( [1, -1] ) )
            turtle.forward(10)

        for j in range( random.randint(20, 40) ):
            terp.setColor( (random.random(), random.random(), 0.1) )
            terp.place( x0 + random.gauss( 0, 40 ), y0 + random.gauss( 0, 5 ), random.randint(0, 360) )
            terp.drawString( 'L', random.randint( 3, 5 ), 90 )

    terp.hold()


if __name__ == "__main__":
    main()

