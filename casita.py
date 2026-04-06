from pygame import *
import sys 

init()

window = display.set_mode((1280, 720))

window.fill((152, 209, 255))

while (True):
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()

    # desenho
    draw.rect(window, (0, 153, 0), (0, 550, 1280, 300))
    draw.rect(window,(96, 96, 96), (400, 350, 200, 200))
    draw.rect(window,(102, 51, 0), (500, 400, 80, 150))
    draw.rect(window,(0, 0, 153), (420, 430, 50, 50))
    draw.circle(window, (255, 255, 0), (170, 140), 60)
    draw.circle(window, (255, 255, 255), (800, 130), 60)
    draw.circle(window, (255, 255, 255), (900, 130), 60)
    draw.circle(window, (255, 255, 255), (1000, 130), 60)
    draw.circle(window, (255, 255, 255), (1100, 130), 60) 

    display.update()