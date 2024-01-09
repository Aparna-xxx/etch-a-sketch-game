from turtle import Turtle, Screen

tim=Turtle()
screen=Screen()

def move_foward():
    tim.forward(10)
def move_left():
    tim.left(10)

def move_right():
    tim.right(10)

def move_down():
   tim.backward(10)

def clr_scr():
    #tim.reset()
    screen.resetscreen()
    tim.left(90);

screen.listen()
tim.left(90);
screen.onkeypress(key="w",fun=move_foward)
screen.onkeypress(key="a",fun=move_left)
screen.onkeypress(key="s",fun=move_down)
screen.onkeypress(key="d",fun=move_right)
screen.onkey(key="c",fun=clr_scr)
screen.exitonclick()