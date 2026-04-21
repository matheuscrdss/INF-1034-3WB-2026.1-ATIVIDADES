from pygame import *

init()

window = display.set_mode((1280, 720))
clock = time.Clock()
running = True

fonte = font.Font("Atividade 6/animeace2_bld.otf", 30)
image_spider = image.load("Atividade 6/spiderman.png")
image_spider = transform.scale(image_spider, (200, 200))

mixer.music.load("Atividade 6/spiderman.mp3")
mixer.music.play(-1)

x_nuvem = 800
direcao_nuvem = 1
vel_nuvem = 5
largura_nuvem = 300

x_sol = 170
y_sol = 140
raio_sol = 60
vel_sol = 5

texto = "I am Spider Man!"

while running:
    clock.tick(60)

    for ev in event.get():
        if ev.type == QUIT:
            running = False

        if ev.type == MOUSEMOTION:
            x_sol, y_sol = ev.pos

        if ev.type == MOUSEBUTTONUP:
            if ev.button == 1:
                texto = "I said I am Spider Man!"
            elif ev.button == 3:
                texto = "I am Spider Man!"

    keys = key.get_pressed()

    if keys[K_a] or keys[K_LEFT]:
        x_sol -= vel_sol
    if keys[K_d] or keys[K_RIGHT]:
        x_sol += vel_sol
    if keys[K_w] or keys[K_UP]:
        y_sol -= vel_sol
    if keys[K_s] or keys[K_DOWN]:
        y_sol += vel_sol

    if x_sol < raio_sol:
        x_sol = raio_sol
    if x_sol > 1280 - raio_sol:
        x_sol = 1280 - raio_sol
    if y_sol < raio_sol:
        y_sol = raio_sol
    if y_sol > 720 - raio_sol:
        y_sol = 720 - raio_sol

    x_nuvem += vel_nuvem * direcao_nuvem

    if x_nuvem + largura_nuvem >= 1280:
        direcao_nuvem = -1
    if x_nuvem <= 0:
        direcao_nuvem = 1

    if y_sol < 200:
        cor = (152, 209, 255)

    elif y_sol < 450:
        t = (y_sol - 200) / 250

        x = int(152 + (255 - 152) * t)
        y = int(209 + (140 - 209) * t)
        z = int(255 + (0 - 255) * t)

        cor = (x,y,z)

    else:
        t = (y_sol - 450) / 270

        x = int(255 + (10 - 255) * t)
        y = int(140 + (10 - 140) * t)
        z = int(0 + (60 - 0) * t)

        cor = (x,y,z)

    window.fill(cor)

    draw.rect(window, (0, 153, 0), (0, 550, 1280, 300))
    draw.rect(window, (96, 96, 96), (400, 350, 200, 200))
    draw.rect(window, (102, 51, 0), (500, 400, 80, 150))
    draw.rect(window, (0, 0, 153), (420, 430, 50, 50))

    draw.circle(window, (255, 255, 0), (x_sol, y_sol), raio_sol)

    draw.line(window, (255, 255, 0), (x_sol, y_sol - 60), (x_sol, y_sol - 100), 8)
    draw.line(window, (255, 255, 0), (x_sol, y_sol + 60), (x_sol, y_sol + 100), 8)
    draw.line(window, (255, 255, 0), (x_sol + 60, y_sol), (x_sol + 100, y_sol), 8)
    draw.line(window, (255, 255, 0), (x_sol - 60, y_sol), (x_sol - 100, y_sol), 8)
    draw.line(window, (255, 255, 0), (x_sol + 40, y_sol - 40), (x_sol + 70, y_sol - 70), 8)
    draw.line(window, (255, 255, 0), (x_sol - 40, y_sol - 40), (x_sol - 70, y_sol - 70), 8)
    draw.line(window, (255, 255, 0), (x_sol + 40, y_sol + 40), (x_sol + 70, y_sol + 70), 8)
    draw.line(window, (255, 255, 0), (x_sol - 40, y_sol + 40), (x_sol - 70, y_sol + 70), 8)

    for i in range(4):
        draw.circle(window, (255, 255, 255), (x_nuvem + (i * 70), 130), 60)

    draw.polygon(window, (153, 0, 0), [(500, 200), (400, 350), (600, 350)])
    draw.circle(window, (102, 204, 0), (510, 480), 5)
    draw.rect(window, (102, 51, 0), (975, 450, 50, 100))
    draw.circle(window, (0, 102, 0), (1000, 380), 80)

    window.blit(image_spider, (50, 400))

    steve_text = fonte.render(texto, True, "#000000")
    window.blit(steve_text, (30, 300))

    display.update()