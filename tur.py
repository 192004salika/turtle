import turtle
t=turtle.Turtle()
t.shape('turtle')
t.speed(5)
colorList=['red','blue','pink','yellow','black','green','brown']
for i in range(36):
    for colors in colorList:
        t.pencolor(colors)
        t.circle(100)
        t.left(100)


turtle.done()

