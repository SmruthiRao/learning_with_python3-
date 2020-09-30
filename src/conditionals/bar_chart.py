import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

def draw_barchart(t,ht):
    t.begin_fill()
    t.left(90)
    t.forward(ht)
    t.write(" "+str(ht))
    t.right(90)
    t.forward(15)
    t.right(90)
    t.forward(ht)
    t.left(90)
    t.end_fill()
    t.forward(15)



tess = turtle.Turtle()
tess.color("blue", "red")
tess.pensize(5)

xs = [20,30,10,50,25]

for i in xs:
    draw_barchart(tess,i)

wn.mainloop()


