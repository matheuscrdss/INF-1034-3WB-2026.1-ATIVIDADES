from turtle import *
import time

t = Turtle()
t.speed(0)

#japao - facil 

t.pencolor('black')
t.fillcolor('white')
t.begin_fill()


for i in range(2):
    t.fd(300)
    t.lt(90)
    t.fd(200)
    t.lt(90)

t.end_fill()

t.pu()
t.goto(150,60)
t.pd()


t.fillcolor('red')
t.begin_fill()
t.circle(50)
t.end_fill()

time.sleep(3)
t.clear()

t.pu()
t.goto(0,0)
t.pd()

# # italia - facil

t.fillcolor('black')
t.begin_fill()


for i in range(2):
    t.fd(300)
    t.lt(90)
    t.fd(200)
    t.lt(90)

t.fillcolor('green')
t.begin_fill()
for i in range(2):
    t.fd(100)
    t.lt(90)
    t.fd(100)
t.end_fill()


t.pu()
t.goto(0,0)
t.pd()
t.lt(180)
t.fd(200)

t.fillcolor('red')
t.begin_fill()

for i in range(2):
    t.fd(100)
    t.lt(90)
    t.fd(100)
t.lt(90)
t.fd(200)

t.end_fill()

time.sleep(3)
t.clear()

t.reset()
t.speed(0)
t.pu()
t.goto(0,0)
t.pd()

# irlanda - facil

t.fillcolor('black')
t.begin_fill()


for i in range(2):
    t.fd(300)
    t.lt(90)
    t.fd(200)
    t.lt(90)

t.fillcolor('green')
t.begin_fill()
for i in range(2):
    t.fd(100)
    t.lt(90)
    t.fd(100)
t.end_fill()


t.pu()
t.goto(0,0)
t.pd()
t.lt(180)
t.fd(200)

t.fillcolor('orange')
t.begin_fill()

for i in range(2):
    t.fd(100)
    t.lt(90)
    t.fd(100)
t.lt(90)
t.fd(200)

t.end_fill()

time.sleep(3)
t.clear()

t.reset()
t.speed(0)
t.pu()
t.goto(0,0)
t.pd()

# ucrania - facil

for i in range(2):
    t.fd(300)
    t.lt(90)
    t.fd(200)
    t.lt(90)

t.fillcolor('yellow')
t.begin_fill()

for i in range(2):
    t.fd(300)
    t.lt(90)
    t.fd(100)
    t.lt(90)

t.end_fill()

t.lt(90)
t.fd(100)
t.right(90)

t.fillcolor('blue')
t.begin_fill()

for i in range(2):
    t.fd(300)
    t.lt(90)
    t.fd(100)
    t.lt(90)

t.end_fill()

time.sleep(3)
t.clear()

# polonia - facil 

t.reset()
t.speed(0)

for i in range(2):
    t.fd(300)
    t.lt(90)
    t.fd(200)
    t.lt(90)

t.fillcolor('red')
t.begin_fill()

for i in range(2):
    t.fd(300)
    t.lt(90)
    t.fd(100)
    t.lt(90)

t.end_fill()

t.lt(90)
t.fd(100)
t.right(90)

t.fillcolor('white')
t.begin_fill()

for i in range(2):
    t.fd(300)
    t.lt(90)
    t.fd(100)
    t.lt(90)

t.end_fill()

time.sleep(3)
t.clear()

# #india - dificil

t.reset()
t.speed(0)

for i in range(2):
    t.fd(300)
    t.lt(90)
    t.fd(200)
    t.lt(90)

t.fillcolor('green')
t.begin_fill()

for i in range(2):
    t.fd(300)
    t.lt(90)
    t.fd(70)
    t.lt(90)

t.end_fill()

t.pu()
t.goto(0,0)
t.pd()
t.lt(90)
t.fd(130)
t.right(90)

t.fillcolor('orange')
t.begin_fill()

for i in range(2):
    t.fd(300)
    t.lt(90)
    t.fd(70)
    t.lt(90)

t.end_fill()

t.pu()
t.goto(150,80)
t.pd()

t.pensize(2)
t.circle(20)

t.fillcolor('dark blue')

for i in range(24):
    t.pu()
    t.goto(150, 100)
    t.setheading(i * 15)
    t.forward(10)
    t.pd()
    t.bk(10)
t.end_fill()

time.sleep(3)
t.clear()

# #emirados arabes - medio

t.reset()
t.speed(0)

t.pencolor('black')
t.fillcolor('black')
t.begin_fill()


for i in range(2):
    t.fd(300)
    t.lt(90)
    t.fd(200)
    t.lt(90)

t.fillcolor('red')
t.begin_fill()
for i in range(2):
    t.fd(100)
    t.lt(90)
    t.fd(100)
t.end_fill()

t.pu()
t.goto(0,0)
t.pd()
t.lt(180)
t.fd(100)

t.fillcolor('black')
t.begin_fill()

for i in range(2):
    t.fd(200)
    t.lt(90)
    t.fd(65)
    t.lt(90)

t.end_fill()

t.lt(90)
t.fd(200)
t.right(90)

t.fillcolor('green')
t.begin_fill()

for i in range(2):
    t.fd(200)
    t.right(90)
    t.fd(65)
    t.right(90)

t.end_fill()

time.sleep(3)
t.clear()

# #senegal - medio

t.reset()
t.speed(0)

t.fillcolor('black')
t.begin_fill()


for i in range(2):
    t.fd(300)
    t.lt(90)
    t.fd(200)
    t.lt(90)

t.fillcolor('green')
t.begin_fill()
for i in range(2):
    t.fd(100)
    t.lt(90)
    t.fd(100)
t.end_fill()


t.pu()
t.goto(0,0)
t.pd()
t.lt(180)
t.fd(200)

t.fillcolor('red')
t.begin_fill()

for i in range(2):
    t.fd(100)
    t.lt(90)
    t.fd(100)
t.lt(90)
t.fd(200)

t.end_fill()

t.pu()
t.goto(0,0)
t.pd()
t.lt(90)
t.fd(100)

t.fillcolor('yellow')
t.begin_fill()

for i in range(2):
    t.fd(100)
    t.lt(90)
    t.fd(200)
    t.lt(90)

t.end_fill()

t.pu()
t.goto(120,110)
t.pd()

t.fillcolor('green')
t.begin_fill()

for i in range(5):
    t.fd(60)
    t.right(144)

t.end_fill()

t.pu()
t.goto(150,90)
t.pd()

t.fillcolor('green')
t.begin_fill()
t.pencolor('green')
t.circle(11)
t.pencolor('black')
t.end_fill()

time.sleep(3)
t.clear()

# # palestina - medio

t.reset()
t.speed(0)

for i in range(2):
    t.fd(300)
    t.lt(90)
    t.fd(200)
    t.lt(90)


t.fillcolor('green')
t.begin_fill()

for i in range(2):
    t.fd(300)
    t.lt(90)
    t.fd(70)
    t.lt(90)

t.end_fill()

t.lt(90)
t.fd(200)
t.right(90)

t.fillcolor('black')
t.begin_fill()

for i in range(2):
    t.fd(300)
    t.right(90)
    t.fd(70)
    t.right(90)

t.end_fill()

t.fillcolor('red')
t.begin_fill()

t.right(45)
t.fd(150)
t.right(90)
t.fd(150)

t.end_fill()

time.sleep(3)
t.clear

# bahamas - medio

t.reset()
t.speed(0)

for i in range(2):
    t.fd(300)
    t.lt(90)
    t.fd(200)
    t.lt(90)


t.fillcolor('#316882')
t.begin_fill()

for i in range(2):
    t.fd(300)
    t.lt(90)
    t.fd(70)
    t.lt(90)

t.end_fill()

t.lt(90)
t.fd(200)
t.right(90)

t.fillcolor('#316882')
t.begin_fill()

for i in range(2):
    t.fd(300)
    t.right(90)
    t.fd(70)
    t.right(90)

t.end_fill()

t.right(90)
t.fd(70)
t.lt(90)

t.fillcolor('yellow')
t.begin_fill()

for i in range(2):
    t.fd(300)
    t.right(90)
    t.fd(60)
    t.right(90)

t.end_fill()

t.lt(90)
t.fd(70)
t.right(90)

t.fillcolor('black')
t.begin_fill()

t.right(45)
t.fd(150)
t.right(90)
t.fd(150)

t.end_fill()

time.sleep(3)
t.clear()

# sudao - medio

t.reset()
t.speed(0)

for i in range(2):
    t.fd(300)
    t.lt(90)
    t.fd(200)
    t.lt(90)


t.fillcolor('black')
t.begin_fill()

for i in range(2):
    t.fd(300)
    t.lt(90)
    t.fd(70)
    t.lt(90)

t.end_fill()

t.lt(90)
t.fd(200)
t.right(90)

t.fillcolor('red')
t.begin_fill()

for i in range(2):
    t.fd(300)
    t.right(90)
    t.fd(70)
    t.right(90)

t.end_fill()

t.fillcolor('green')
t.begin_fill()

t.right(45)
t.fd(150)
t.right(90)
t.fd(150)

t.end_fill()

time.sleep(3)
t.clear()

# camaroes - medio

t.reset()
t.speed(0)

t.fillcolor('black')
t.begin_fill()


for i in range(2):
    t.fd(300)
    t.lt(90)
    t.fd(200)
    t.lt(90)

t.fillcolor('green')
t.begin_fill()
for i in range(2):
    t.fd(100)
    t.lt(90)
    t.fd(100)
t.end_fill()


t.pu()
t.goto(0,0)
t.pd()
t.lt(180)
t.fd(200)

t.fillcolor('yellow')
t.begin_fill()

for i in range(2):
    t.fd(100)
    t.lt(90)
    t.fd(100)
t.lt(90)
t.fd(200)

t.end_fill()

t.lt(180)

t.fillcolor('red')
t.begin_fill()

for i in range(2):
    t.fd(200)
    t.lt(90)
    t.fd(100)
    t.lt(90)

t.end_fill()

t.pu()
t.goto(120,110)
t.pd()
t.right(90)

t.fillcolor('yellow')
t.begin_fill()

for i in range(5):
    t.fd(60)
    t.right(144)

t.end_fill()

t.pu()
t.goto(150,90)
t.pd()

t.fillcolor('yellow')
t.begin_fill()
t.pencolor('yellow')
t.circle(11)
t.pencolor('black')
t.end_fill()

time.sleep(3)
t.clear()

mainloop()