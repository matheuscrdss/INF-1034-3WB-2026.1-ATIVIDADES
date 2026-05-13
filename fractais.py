from turtle import *

t = Turtle()
t.speed(5)


for i in range(100):
    t.fd(i)
    t.lt(15)

t.clear()


def quadrado(x, y, tamanho, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for i in range(4):
        t.fd(tamanho)
        t.lt(90)
    t.end_fill()

for i in range(6):
    quadrado = quadrado( )