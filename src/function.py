import turtle

def draw_square(t,sz):
    """ make turtle draw a square"""
    for i in range(4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Turtle draws a square")

alex = turtle.Turtle()
draw_square(alex,50)

wn.mainloop()