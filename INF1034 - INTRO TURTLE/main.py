from turtle import *

t = Turtle()

color = textinput('Escolhe uma cor', 'Digite: ')
t.speed(100)

# CARTESIANO
t.fillcolor(color)
t.begin_fill()

t.fd(500)
t.pu()
t.goto(0,0)
t.pd()
t.back(500)

t.pu()
t.goto(0,0)
t.pd()
t.lt(90)
t.fd(500)

t.pu()
t.goto(0,0)
t.pd()
t.back(500)

t.goto(0,0)
t.end_fill()

#octagono
t.pu()
t.goto(350,150)
t.pd()

t.fillcolor(color)
t.begin_fill()
for i in range(8):
    t.fd(100)
    t.lt(45)
t.end_fill()

#losango
t.pu()
t.goto(-300,-200)
t.pd()
t.setheading(0)

t.fillcolor(color)
t.begin_fill()
for i in range(2):
    t.fd(150)   
    t.lt(60)
    t.fd(150)   
    t.lt(120)
t.end_fill()

# triangulo
t.pu()
t.goto(150,-200)
t.pd()
t.setheading(0)

t.fillcolor(color)
t.begin_fill()
for i in range(3):
    t.fd(150)
    t.lt(120)
t.end_fill()

#retangulo
t.pu()
t.goto(-300,150)
t.pd()
t.setheading(0)

t.fillcolor(color)
t.begin_fill()
for i in range(2):
    t.fd(200)
    t.lt(90)
    t.fd(100)
    t.lt(90)
t.end_fill()

mainloop()