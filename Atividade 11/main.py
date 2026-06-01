import pygame

pygame.init()

largura = 900
altura = 700
chao = 350

tela = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()

img = pygame.image.load("Atividade 11/spiderman.png").convert()

cor_transparente = img.get_at((0,0))
img.set_colorkey(cor_transparente)

larg_sprite = img.get_width() // 3
alt_sprite = 220

sprites_dir = []
sprites_esq = []

for pos in range(3):

    corte = img.subsurface(pos * larg_sprite, 0, larg_sprite, alt_sprite)

    corte = pygame.transform.scale(corte,(90,90))

    sprites_dir.append(corte)
    sprites_esq.append(pygame.transform.flip(corte,True,False))

sprite_idle = pygame.transform.scale(img.subsurface(0,0,larg_sprite,alt_sprite),(90,90))

sprite_jump = pygame.transform.scale(
    img.subsurface(larg_sprite, alt_sprite+30, larg_sprite, alt_sprite-30),(90,90))

parte_teia = img.subsurface(0, img.get_height() - img.get_height()//3, img.get_width()//2, img.get_height()//3)

sprite_teia_dir = pygame.transform.scale(parte_teia,(130,90))
sprite_teia_esq = pygame.transform.flip(sprite_teia_dir, True, False)

x = 100
y = chao

velocidade_x = 5

gravidade = 1
forca_pulo = -16
velocidade_y = 0

olhando = 1   

pulando = False
usando_teia = False

frame = 0
contador_anim = 0

rodando = True

while rodando:

    dt = clock.tick(60)

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_SPACE:

                if not pulando:

                    pulando = True
                    velocidade_y = forca_pulo

    teclas = pygame.key.get_pressed()

    dx = 0

    if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:

        dx += velocidade_x
        olhando = 1

    if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:

        dx -= velocidade_x
        olhando = -1

    usando_teia = teclas[pygame.K_e]

    x += dx

    if x < 0:
        x = 0

    if x > largura-90:
        x = largura-90

    if pulando:

        y += velocidade_y

        velocidade_y += gravidade

        if y >= chao:

            y = chao

            pulando = False
            velocidade_y = 0

    if dx != 0 and not pulando and not usando_teia:

        contador_anim += 1

        if contador_anim > 5:

            frame += 1

            if frame >= len(sprites_dir):
                frame = 0

            contador_anim = 0

    else:

        frame = 0

    if usando_teia:

        sprite = sprite_teia_dir if olhando == 1 else sprite_teia_esq

        pos_x = x if olhando == 1 else x-40
        pos_y = y+26

    elif pulando:

        sprite = sprite_jump
        pos_x = x
        pos_y = y

    elif dx != 0:

        sprite = sprites_dir[frame] if olhando == 1 else sprites_esq[frame]

        pos_x = x
        pos_y = y

    else:

        sprite = sprite_idle

        pos_x = x
        pos_y = y


    tela.fill((200,230,255))

    pygame.draw.rect(tela, (0, 153, 0), (0,chao+90,largura,altura))

    tela.blit(sprite,(pos_x,pos_y))

    pygame.display.flip()

pygame.quit()