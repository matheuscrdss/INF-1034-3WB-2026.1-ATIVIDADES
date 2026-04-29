from pygame import *
import sys

init()

window = display.set_mode((500, 720))
clock = time.Clock()
running = True

while running:
    clock.tick(60)

    for ev in event.get():
        if ev.type == QUIT:
            running = False

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b


num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

escolha = input("Digite sua escolha [-, +, x, /]:  ")

if escolha == "+":
    print(soma(num1, num2))    
elif escolha == "-":
    print(subtracao(num1, num2))
elif escolha == "x":
    print(multiplicacao(num1, num2))
elif escolha == "/":
    print(divisao(num1, num2))

display.update()
sys.exit()