from turtle import *
import random as rd

t = Turtle()
t.speed(0)

color = textinput('Escolher a cor', 'Digite cor desejada: ')


# desenhar o plano cartesiano
def cartesiano():
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


x = rd.randint(100, 300)
y = rd.randint(0, 300)
x1 = rd.randint(-300, 0)
y1 = rd.randint(-300, 0)



# desenhar um quadrado
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


# desenhar um octogono
def octogono(x1, y, tamanho, color):
    t.pu()
    t.goto(x1, y)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for i in range(8):
        t.fd(tamanho)
        t.lt(45)
    t.end_fill()

# #desenhar um triangulo
def triangulo(x, y1, tamanho,color):
    t.pu()
    t.goto(x, y1)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for i in range(3):
        t.fd(tamanho)
        t.lt(120)
    t.end_fill()


# # desenhar um retangulo
def retangulo(x1, y1, tamanho, color):
    t.pu()
    t.goto(x1, y1)
    t.pd()
    t.begin_fill()
    t.fillcolor(color)
    for i in range(2):
        t.fd(tamanho)
        t.lt(90)
        t.fd(200)
        t.lt(90)
    t.end_fill()


cartesiano()

quadrado(x, y, 100, color)
octogono(x1, y, 50, color)
triangulo(x, y1, 100, color)
retangulo(x1, y1, 100, color)




mainloop()