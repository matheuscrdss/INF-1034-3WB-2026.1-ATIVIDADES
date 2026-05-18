from turtle import *
from random import randint
from time import sleep

colormode(255)

t = Turtle()
t.speed(0)


def corAleatoria():
    return (randint(0, 255), randint(0, 255), randint(0, 255))


#facil
def desenhaCirculo(quantidade):
    t.clear()
    t.pu()
    t.goto(0, 0)
    t.setheading(0)
    t.pd()

    for i in range(quantidade):
        t.circle(i)
        t.lt(20)


def mudarCirculo():
    quantidade = numinput("Alterar circulo", "Digite a quantidade de círculos:")

    if quantidade is not None:
        desenhaCirculo(int(quantidade))


# medio
def desenhaTriangulo(t, tamanho):
    t.pd()
    t.begin_fill()
    t.fillcolor(corAleatoria())

    for i in range(3):
        t.fd(tamanho)
        t.lt(120)

    t.end_fill()
    t.pu()


def fractalTriangulo(t, tamanho, angulo, nivel):
    if nivel <= 0 or tamanho < 5:
        return

    t.pencolor(corAleatoria())
    desenhaTriangulo(t, tamanho)

    t.fd(tamanho / 2)
    t.lt(angulo)

    fractalTriangulo(t, tamanho * 0.85, angulo, nivel - 1)


def desenhaFractalTriangulo(angulo):
    t.clear()
    t.pu()
    t.goto(0, 0)
    t.setheading(0)
    t.pd()

    fractalTriangulo(t, 120, angulo, 35)


def mudarTriangulo():
    angulo = numinput("Alterar triangulo", "Digite o ângulo:")

    if angulo is not None:
        desenhaFractalTriangulo(angulo)


# dificil
def fractalArvore(t, tamanho, angulo, nivel):
    if nivel <= 0 or tamanho < 20:
        return

    t.pd()

    t.fd(tamanho)

    t.lt(angulo)
    fractalArvore(t, tamanho * 0.7, angulo, nivel - 1)

    t.rt(angulo)
    fractalArvore(t, tamanho * 0.75, angulo, nivel - 1)

    t.rt(angulo)
    fractalArvore(t, tamanho * 0.7, angulo, nivel - 1)

    t.lt(angulo)
    t.back(tamanho)


def desenhaArvore(angulo):
    t.clear()
    t.pu()
    t.goto(0, -250)
    t.setheading(90)
    t.pd()

    fractalArvore(t, 90, angulo, 6)


def mudarArvore():
    angulo = numinput("Alterar angulo", "Digite o ângulo da árvore:")

    if angulo is not None:
        desenhaArvore(angulo)

desenhaCirculo(100)
mudarCirculo()

sleep(2)

desenhaFractalTriangulo(18)
mudarTriangulo()

sleep(2)

desenhaArvore(30)
mudarArvore()

mainloop()