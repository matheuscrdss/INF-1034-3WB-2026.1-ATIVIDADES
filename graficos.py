from turtle import *

def soma_10(x):
    return x + 10

def ex_1(x):
    return x * 0.5

def ex_2(x):
    return 1 / x

def ex_4(x):
    return 5 - x ** 2 

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

# t.color("red")
# t.pu()
# t.goto(-100, soma_10(-100))
# t.pd()
# t.goto(100, soma_10(100))

# O range vai do primeiro valor até o último -1
# print(list(range(-100, 100)))

# for x in range(-100, 100):
#     print(x)


# plano_cartesiano()
# t.color("blue")
# t.pu()
# t.goto(-200, soma_10(-200))
# t.pd()
# for x in range(-99, 101):
#     t.goto(2 * x, soma_10(2*x))
# t.clear()

# plano_cartesiano()
# t.color("blue")
# t.pu()
# t.goto(0, raiz_X(0))
# t.pd()
# for x in range(0, 101):
#     t.goto(2 * x, raiz_X(x * 2))

# plano_cartesiano()
# t.color("blue")
# t.pu()
# t.goto(0, sob_X(0))
# t.pd()
# for x in range(0, 101):
#     t.goto(2 * x, sob_X(x * 2))

plano_cartesiano()
t.color("blue")
t.pu()
t.goto(0, -200)
t.pd()
for x in range(-50,200):
    t.goto(2 * x, ex_4(x * 2))

    




mainloop()