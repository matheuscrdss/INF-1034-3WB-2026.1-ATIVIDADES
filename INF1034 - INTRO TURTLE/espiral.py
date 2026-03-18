from turtle import *

t = Turtle()

color = textinput('Escolhe uma cor', 'Digite: ')
t.speed(100)

#espiral
t.pu()
t.goto(0,0)
t.pd()

t.fillcolor(color)
t.begin_fill()
for i in range(100):
    t.fd(i * 2)
    t.lt(90)

t.end_fill()
mainloop()