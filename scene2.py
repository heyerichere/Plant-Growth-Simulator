'''scene2.py
12/10/2022
CS151 F22  Final project
Eric Appiah'''


import graphicsPlus as gr


class Environmental:
    '''Initializes Environmental class with a fish and sun_list field'''
    def __init__(self):
        self.fish = []
        self.sun_list = []


    def fish_init(self,x,y):
        '''creates fishes'''
        head1 = gr.Polygon(gr.Point(x+40,y), gr.Point(x,y+40), gr.Point(x,y-40))
        head1.setFill("saddle brown")
        self.fish.append(head1)
        eye1 = gr.Circle(gr.Point(x+20,y-10),5)
        self.fish.append(eye1)
        eye2 = gr.Circle(gr.Point(x+22,y-9),2)
        eye2.setFill("Black")
        self.fish.append(eye2)
        mouth1 = gr.Line(gr.Point(x+40,y),gr.Point(x+25,y))
        self.fish.append(mouth1)
        fin1 = gr.Polygon(gr.Point(x-20,y-20), gr.Point(x,y), gr.Point(x-20, y+20),gr.Point(x-10,y))
        fin1.setFill("black")
        self.fish.append(fin1)
        return  self.fish


    def rect(self,x,y):
        '''creates rectangle shape'''
        self.rect1 = gr.Rectangle(gr.Point(x,y), gr.Point(x+1000,y-600))
        self.rect1.setFill("light blue")
        return self.rect1


    def sun_init(self,x,y):
        '''creates the sun as a complex shape'''
        self.sun = gr.Circle(gr.Point(x,y),50)
        self.sun.setFill("orange")
        self.sun_list.append(self.sun)
        self.line1 = gr.Line(gr.Point(x+55,y),gr.Point(x+75,y))
        self.sun_list.append(self.line1)
        self.line2 = gr.Line(gr.Point(x,y+55),gr.Point(x,y+75))
        self.sun_list.append(self.line2)
        self.line3 = gr.Line(gr.Point(x-55,y),gr.Point(x-75,y))
        self.sun_list.append(self.line3)
        self.line4 = gr.Line(gr.Point(x,y-55),gr.Point(x,y-75))
        self.sun_list.append(self.line4)
        self.line5 = gr.Line(gr.Point(x+45,y-35), gr.Point(x+65,y-45))
        self.sun_list.append(self.line5)
        self.line6 = gr.Line(gr.Point(x-45,y+35), gr.Point(x-65,y+45))
        self.sun_list.append(self.line6)
        self.line7 = gr.Line(gr.Point(x-45,y-35), gr.Point(x-65,y-45))
        self.sun_list.append(self.line7)
        self.line8 = gr.Line(gr.Point(x+45,y+35), gr.Point(x+65, y+45))
        self.sun_list.append(self.line8)
        return self.sun_list


    def Draw(self, shapes, win):
        '''Draws objects and shapes'''
        for shape in shapes:
            shape.draw(win)
        

    def fish_animate(self, fish, frame, screen):
        '''Move the self.fish at the current iteration of the animation (frame).'''
        if frame %2 == 0:
            for shape in self.fish:
                shape.move(10,5)
        if frame %2 == 1:
            for shape in self.fish:
                shape.move(-10,5)
        screen.update()
        
        
def main(obj):
    '''creates scene 2'''
    win = gr.GraphWin("SCENE TWO",1000,1000)
    rect2 = obj.rect(0,1000)
    sun = obj.sun_init(800,100)
    rect2.draw(win)
    obj.Draw(sun, win)
    x = 100
    for i in range(2):
        for x in range(100,800,100):
            fishes1 = obj.fish_init(x,500)
            fishes2 = obj.fish_init(x,600)
            fishes3 = obj.fish_init(x,700)
            obj.Draw(fishes1, win)
            for item in fishes1:
                item.undraw()
            for item in fishes2:
                item.undraw()
            for item in fishes3:
                item.undraw()
            obj.fish_animate(fishes1, x, win)
            obj.fish_animate(fishes2, x, win)
            obj.fish_animate(fishes3, x, win)
            win.update()
    win.getMouse()
    win.close()


if __name__ == "__main__":
    environmental = Environmental()
    main(environmental)