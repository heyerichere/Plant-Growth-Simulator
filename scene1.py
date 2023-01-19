'''scene1.py
12/10/2022
CS151 F22  Final project
Eric Appiah'''


import graphicsPlus as gr


def sun_init(x,y):
    '''creates the sun as a complex shape'''
    sun_list = []
    sun = gr.Circle(gr.Point(x,y),50)
    sun.setFill("orange")
    sun_list.append(sun)
    line1 = gr.Line(gr.Point(x+55,y),gr.Point(x+75,y))
    sun_list.append(line1)
    line2 = gr.Line(gr.Point(x,y+55),gr.Point(x,y+75))
    sun_list.append(line2)
    line3 = gr.Line(gr.Point(x-55,y),gr.Point(x-75,y))
    sun_list.append(line3)
    line4 = gr.Line(gr.Point(x,y-55),gr.Point(x,y-75))
    sun_list.append(line4)
    line5 = gr.Line(gr.Point(x+45,y-35), gr.Point(x+65,y-45))
    sun_list.append(line5)
    line6 = gr.Line(gr.Point(x-45,y+35), gr.Point(x-65,y+45))
    sun_list.append(line6)
    line7 = gr.Line(gr.Point(x-45,y-35), gr.Point(x-65,y-45))
    sun_list.append(line7)
    line8 = gr.Line(gr.Point(x+45,y+35), gr.Point(x+65, y+45))
    sun_list.append(line8)
    return sun_list


def Draw(shapes, win):
    '''Draws objects and shapes'''
    for shape in shapes:
        shape.draw(win)


def mount():
    '''inserts the graphed data set as a mountain'''
    win = gr.GraphWin("SCENE ONE",1000,1000)
    sun = sun_init(100,100)
    pic1 = gr.Image(gr.Point(500, 400), "graph.gif")
    pic1.draw(win)
    Draw(sun, win)
    win.getMouse()
    win.close()


if __name__ == "__main__":
    mount()