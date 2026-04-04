from turtle import *
from time import sleep
import math


def ex_1(x):
    return math.sqrt(x)

def ex_2(x):
    return 1 / x

def ex_3(x):
    return 2 ** x

def ex_4(x):
    return 5 - x ** 2 

def ex_5(x):
    return x ** 2 - 5*x + 6

def ex_6(x):
    return x**3 - x**2 - x + 1

t = Turtle()
t.speed(0)


def plano_cartesiano():
    # Eixo dos X
    t.pu()
    t.goto(-300, 0)
    t.pd()
    t.goto(300, 0)
    t.stamp()

    # Eixo dos Y
    t.pu()
    t.goto(0, -300)
    t.pd()
    t.goto(0, 300)
    t.lt(90)
    t.stamp()

# ex 1 

plano_cartesiano()
t.color("red")
t.pu()
t.goto(0, ex_1(0))
t.pd()

for x in range(0, 150):
    y = ex_1(x)
    t.goto(2 * x, 2 * y)

sleep(3)
t.clear()


# ex 2 

t.color('black')
plano_cartesiano()
t.color('red')
t.pu()
for x in range(1, 101):
    y = ex_2(x / 10)
    t.goto((x / 10) * 50, y * 50)
    t.pd()
t.pu()
for x in range(-100, 0):
    y = ex_2(x / 10)
    t.goto((x / 10) * 50, y * 50)
    t.pd()
sleep(3)
t.clear()


# ex 3 

t.color('black')
plano_cartesiano()
t.speed(6)
t.color("red")
t.pu()
t.goto(-300, ex_3(-10) * 20)
t.pd()

for x in range(-10, 5):
    t.goto(x * 20, ex_3(x) * 20)
sleep(3)
t.clear()


# ex 4 

t.color('black')
plano_cartesiano()
t.color("red")
t.pu()
t.goto(2 * -50, ex_4(-50))
t.pd()
for x in range(-49, 100):
    t.goto(2 * x, ex_4(x))
sleep(3)
t.clear()

#  ex 5 

t.color('black')
plano_cartesiano()
t.color("red")

t.pu()
t.goto(2 * -10 + 15, 2 * ex_5(-10))
t.pd()

for x in range(-7, 40):
    t.goto(6 * x + 15, 6 * ex_5(x))
sleep(3)
t.clear()

# ex 6 

t.color('black')
plano_cartesiano()
t.color("red")

t.pu()
t.goto(2 * -20, 0.1 * ex_6(-20))
t.pd()

for x in range(-9, 50):
    t.goto(2 * x, 0.1 * ex_6(x))
sleep(3)
t.clear()

mainloop()
