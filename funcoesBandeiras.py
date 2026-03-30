from turtle import * 
from time import sleep

t = Turtle()
t.speed(0)


def retangulo(x, y, larg, alt, color):
    t.pu()
    t.goto(x, y)
    t.pd()

    t.begin_fill()
    t.fillcolor(color)
    for i in range(2):
        t.fd(larg)
        t.rt(90)
        t.fd(alt)
        t.rt(90)
    t.end_fill()


def circulo(x, y, tamanho, color):
    t.pu()
    t.goto(x, y)
    t.pd()

    t.begin_fill()
    t.fillcolor(color)
    t.circle(tamanho)
    t.end_fill()

def estrela(x, y, tamanho, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    
    t.begin_fill()
    t.fillcolor(color)
    for i in range(5):
        t.fd(tamanho)
        t.rt(144)
    t.end_fill()
    circulo(-150, 90, 11, color)
    
def triangulo(x, y, tamanho, color):
    t.pu()
    t.goto(x, y)
    t.pd()

    t.begin_fill()
    t.fillcolor(color)
    t.rt(45)
    for i in range(2):
        t.fd(tamanho)
        t.rt(90)
    t.rt(90)

    t.end_fill()

def espiral(x, y, tamanho, color):
    t.pu()
    t.goto(x, y)
    t.pd()
    
    t.begin_fill()
    t.fillcolor(color)
    for i in range(24):
        t.setheading(i * 15)
        t.forward(tamanho)
        t.pd()
        t.bk(tamanho)
    t.end_fill()

def italia():
    retangulo(-300, 200, 100, 200, "green")
    retangulo(-200, 200, 100, 200, "white")
    retangulo(-100, 200, 100, 200, "red")
    sleep(3)
    t.clear()

def irlanda():
    retangulo(-300, 200, 100, 200, "green")
    retangulo(-200, 200, 100, 200, "white")
    retangulo(-100, 200, 100, 200, "orange")
    sleep(3)
    t.clear()


def japao():
    retangulo(-300, 200, 300, 200, "white")
    circulo(-150, 60, 50, "red")
    sleep(3)
    t.clear()


def ucrania():
    retangulo(-300, 200, 300, 100, "blue")
    retangulo(-300, 100, 300, 100, "yellow")
    sleep(3)
    t.clear()


def polonia():
    retangulo(-300, 200, 300, 100, "white")
    retangulo(-300, 100, 300, 100, "red")
    sleep(3)
    t.clear()


def emirados_arabes():
    retangulo(-300, 200, 100, 200, "red")
    retangulo(-200, 200, 200, 70, "green")
    retangulo(-200, 130, 200, 70, "white")
    retangulo(-200, 70, 200, 70, "black")
    sleep(3)
    t.clear()


def senegal():
    retangulo(-300, 200, 100, 200, "green")
    retangulo(-200, 200, 100, 200, "yellow")
    retangulo(-100, 200, 100, 200, "red")
    estrela(-180, 110, 60, "green")
    sleep(3)
    t.clear()


def palestina():
    retangulo(-300, 250, 300, 70, "black")
    retangulo(-300, 180, 300, 70, "white")
    retangulo(-300, 110, 300, 70, "green")
    triangulo(-300, 250, 150, "red")
    sleep(3)
    t.clear()
    

def bahamas():
    retangulo(-300, 250, 300, 70, "#316882")
    retangulo(-300, 180, 300, 70, "yellow")
    retangulo(-300, 110, 300, 70, "#316882")
    triangulo(-300, 250, 150, "black")
    sleep(3)
    t.clear()


def sudao():
    retangulo(-300, 250, 300, 70, "red")
    retangulo(-300, 180, 300, 70, "white")
    retangulo(-300, 110, 300, 70, "black")
    triangulo(-300, 250, 150, "green")
    sleep(3)
    t.clear()


def camaroes():
    retangulo(-300, 200, 100, 200, "green")
    retangulo(-200, 200, 100, 200, "red")
    retangulo(-100, 200, 100, 200, "yellow")
    estrela(-180, 110, 60, "yellow")
    sleep(3)
    t.clear()


def india():
    retangulo(-300, 200, 300, 60, "orange")
    retangulo(-300, 140, 300, 60, "white")
    retangulo(-300, 80, 300, 60, "green")
    circulo(-150, 90, 20, "white")
    espiral(-150, 110, 11, "dark blue")
    sleep(3)
    t.clear()

italia()
irlanda()
japao()
ucrania()
polonia()
emirados_arabes()
senegal()
palestina()
bahamas()
sudao()
camaroes()
india()

mainloop()