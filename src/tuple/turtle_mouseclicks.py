import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title('turtle moves based on mouse click')
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("purple")
alex = turtle.Turtle()
alex.color("blue")
alex.forward(100)


def h1_for_tess(x,y):
#    print('mouse is at {0},{1}'.format(x,y))
    tess.left(42)
    tess.forward(30)

def h1_for_alex(x,y):
#    print('mouse is at {0},{1}'.format(x,y))
    alex.right(84)
    alex.forward(50)

tess.onclick(h1_for_tess)
alex.onclick(h1_for_alex)
#wn.onclick(h1)
wn.mainloop()
