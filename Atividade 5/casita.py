from pygame import *

init()

window = display.set_mode((1280, 720))

clock = time.Clock()
running = True

fonte = font.Font("Atividade 5/animeace2_bld.otf", 30)
image = image.load("Atividade 5/spiderman.png")
image = transform.scale(image, (200, 200))

mixer.music.load("Atividade 5/spiderman.mp3")
mixer.music.play(-1)

x_nuvem = 800

while running:
    clock.tick(60)

    for ev in event.get():
        if ev.type == QUIT:
            running = False

    dt = clock.get_time()/1000
    keys = key.get_pressed()


    direcao = 1  # 1 = direita, -1 = esquerda

    x_nuvem += 5 * direcao

    if x_nuvem >= 950:
        direcao = -1
    if x_nuvem <= 100:
        direcao = 1


    window.fill((152, 209, 255))
    # desenho
    draw.rect(window, (0, 153, 0), (0, 550, 1280, 300))
    draw.rect(window,(96, 96, 96), (400, 350, 200, 200))
    draw.rect(window,(102, 51, 0), (500, 400, 80, 150))
    draw.rect(window,(0, 0, 153), (420, 430, 50, 50))
    draw.circle(window, (255, 255, 0), (170, 140), 60)
    draw.line(window, (255, 255, 0), (170, 80), (170, 40), 8)
    draw.line(window, (255, 255, 0), (170, 200), (170,240), 8)
    draw.line(window, (255, 255, 0), (230, 140), (260, 140), 8)
    draw.line(window, (255, 255, 0), (110, 140), (80, 140), 8)
    draw.line(window, (255, 255, 0), (210, 100), (240, 70), 8)
    draw.line(window, (255, 255, 0), (130, 100), (100, 70), 8) 
    draw.line(window, (255, 255, 0), (210, 180), (240, 210), 8)  
    draw.line(window, (255, 255, 0), (130, 180), (100, 210), 8)
    for i in range(4):
        draw.circle(window, (255, 255, 255), (x_nuvem + (i * 100), 130), 60)
    draw.polygon(window, (153, 0, 0), [(500, 200), (400, 350), (600, 350)])
    draw.circle(window, (102, 204, 0), (510, 480), 5)
    draw.rect(window, (102, 51, 0), (975, 450, 50, 100))
    draw.circle(window, (0, 102, 0), (1000, 380), 80)

    window.blit(image, (50, 400))

    steve_text = fonte.render("I am Spider Man!", True, "#000000")
    window.blit(steve_text, (30, 300))

    display.update()
