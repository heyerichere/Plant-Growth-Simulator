'''main.py
12/10/2022
CS151 F22  Final project
Eric Appiah'''


import scene1
import scene2
import scene3
import turtle
import tkinter.messagebox


def choice():
    '''asks for the user's choice between message box and terminal reeponse'''
    user_response = input("Do you prefer working with MESSAGE BOX or the TERMINAL ")
    if user_response == "TERMINAL" :
        main()
    elif user_response == "MESSAGE BOX" :
        first()


def main():
    '''asks the user what scene to display'''
    response = input("Do you want to view the Graph scene, Lsystem scene, or Environmental scene?")
    if response == "Graph scene":
        scene1.graph()
    elif response == "Environmental scene":
        environmental = scene2.Environmental()
        scene2.main(environmental)
    elif response == "Lsystem scene":
        scene3.main()


def stop(callback):
    '''this uses a message box for user input'''
    answer = tkinter.messagebox.askyesno('More?', "Do you want to view the next scene?")
    print('answer:', answer)

    if answer:
        callback()
    else:
        turtle.exitonclick()


def first(x=0, y=0):
    '''calls scene 1 from scene1.py'''
    tod.color("red", "green")
    tod.begin_fill()
    scene1.mount()
    tod.end_fill()
    turtle.onscreenclick(lambda x,y:stop(second))


def second(x=0, y=0):
    '''calls scene 2 from scene2.py'''
    tod.reset()
    tod.color("red", "green")
    tod.begin_fill()
    environmental = scene2.Environmental()
    scene2.main(environmental)
    tod.end_fill()
    turtle.onscreenclick(lambda x,y:stop(third))


def third(x=0, y=0):
    '''calls scene 3 from scene3.py'''
    tod.reset()
    tod.color("red", "green")
    tod.begin_fill()
    scene3.main()
    tod.end_fill()
    turtle.exitonclick()


if __name__ == "__main__":
    tod = turtle.Turtle()
    first()
    turtle.mainloop()
