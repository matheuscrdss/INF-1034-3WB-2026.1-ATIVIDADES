
import os
import pygame
import sys

pygame.init()

LARGURA = 800
ALTURA = 600
TAMANHO_TILE = 48
FPS = 60

tela = pygame.display.set_mode((LARGURA, ALTURA))
relogio = pygame.time.Clock()


def criar_tile_chao():
    tile = pygame.Surface((TAMANHO_TILE, TAMANHO_TILE))
    tile.fill((45, 42, 55))
    pygame.draw.rect(tile, (35, 32, 45), (0, 0, TAMANHO_TILE, TAMANHO_TILE), 1)
    pygame.draw.line(tile, (58, 55, 70), (0, TAMANHO_TILE // 3), (TAMANHO_TILE, TAMANHO_TILE // 3), 1)
    pygame.draw.line(tile, (58, 55, 70), (TAMANHO_TILE // 2, TAMANHO_TILE // 3), (TAMANHO_TILE // 2, TAMANHO_TILE), 1)
    return tile


def criar_tile_parede():
    tile = pygame.Surface((TAMANHO_TILE, TAMANHO_TILE))
    tile.fill((88, 50, 28))
    pygame.draw.rect(tile, (65, 33, 12), (1, 1, 22, 10))
    pygame.draw.rect(tile, (65, 33, 12), (25, 13, 22, 10))
    pygame.draw.rect(tile, (65, 33, 12), (1, 25, 22, 10))
    pygame.draw.rect(tile, (65, 33, 12), (25, 37, 22, 10))
    pygame.draw.rect(tile, (48, 22, 5), (0, 0, TAMANHO_TILE, TAMANHO_TILE), 2)
    return tile


def criar_tile_lava():
    tile = pygame.Surface((TAMANHO_TILE, TAMANHO_TILE))
    tile.fill((195, 55, 8))
    pygame.draw.ellipse(tile, (255, 130, 0), (4, 10, 20, 10))
    pygame.draw.ellipse(tile, (255, 210, 0), (26, 27, 15, 7))
    return tile


def criar_tile_bau():
    tile = pygame.Surface((TAMANHO_TILE, TAMANHO_TILE))
    tile.fill((45, 42, 55))
    pygame.draw.rect(tile, (135, 85, 18), (8, 18, 32, 22))
    pygame.draw.rect(tile, (175, 125, 38), (8, 18, 32, 10))
    pygame.draw.circle(tile, (218, 195, 55), (24, 29), 4)
    return tile


def criar_frames_jogador():
    frames = {}
    for direcao in ['baixo', 'cima', 'esquerda', 'direita']:
        lista_frames = []
        for f in range(4):
            img = pygame.Surface((32, 40), pygame.SRCALPHA)

            perna_e = 12 + (4 if f in [1, 3] else 0)
            perna_d = 12 + (4 if f in [0, 2] else 0)
            pygame.draw.rect(img, (18, 18, 32), (8, 26, 7, perna_e))
            pygame.draw.rect(img, (18, 18, 32), (17, 26, 7, perna_d))

            pygame.draw.rect(img, (138, 18, 18), (5, 14, 22, 16))
            pygame.draw.rect(img, (138, 18, 18), (1, 14, 6, 13))
            pygame.draw.rect(img, (138, 18, 18), (25, 14, 6, 13))
            pygame.draw.rect(img, (78, 8, 8), (6, 0, 20, 15))
            pygame.draw.rect(img, (195, 165, 125), (9, 3, 14, 10))

            if direcao == 'baixo':
                pygame.draw.rect(img, (30, 8, 8), (11, 8, 3, 3))
                pygame.draw.rect(img, (30, 8, 8), (18, 8, 3, 3))
            elif direcao == 'esquerda':
                pygame.draw.rect(img, (30, 8, 8), (10, 8, 3, 3))
            elif direcao == 'direita':
                pygame.draw.rect(img, (30, 8, 8), (19, 8, 3, 3))

            lista_frames.append(img)
        frames[direcao] = lista_frames
    return frames


def carregar_mapa(nome_arquivo):
    grade = []
    caminho = os.path.join(os.path.dirname(__file__), nome_arquivo)
    f = open(caminho, 'r')
    for linha in f:
        linha = linha.strip()
        if linha:
            grade.append([int(n) for n in linha.split(',')])
    f.close()
    return grade


def verificar_colisao(retangulo, grade, tiles_solidos):
    for linha in range(len(grade)):
        for coluna in range(len(grade[linha])):
            if grade[linha][coluna] in tiles_solidos:
                rect_tile = pygame.Rect(coluna * TAMANHO_TILE, linha * TAMANHO_TILE, TAMANHO_TILE, TAMANHO_TILE)
                if retangulo.colliderect(rect_tile):
                    return True, rect_tile
    return False, None


tile_chao = criar_tile_chao()
tile_parede = criar_tile_parede()
tile_lava = criar_tile_lava()
tile_bau = criar_tile_bau()

mapa_tiles = {
    0: tile_chao,
    1: tile_parede,
    2: tile_lava,
    3: tile_bau,
}

tiles_solidos = [1, 2]

frames_jogador = criar_frames_jogador()

grade = carregar_mapa('mapa.txt')

LARGURA_MAPA = len(grade[0]) * TAMANHO_TILE
ALTURA_MAPA = len(grade) * TAMANHO_TILE

cam_x = 0
cam_y = 0

LARGURA_JOGADOR = 32
ALTURA_JOGADOR = 40
jogador = pygame.Rect(
    2 * TAMANHO_TILE + (TAMANHO_TILE - LARGURA_JOGADOR) // 2,
    2 * TAMANHO_TILE + (TAMANHO_TILE - ALTURA_JOGADOR) // 2,
    LARGURA_JOGADOR, ALTURA_JOGADOR
)

direcao = 'baixo'
frame_atual = 0
timer_anim = 0
VELOCIDADE = 3

rodando = True
while rodando:
    dt = relogio.tick(FPS)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            rodando = False

    teclas = pygame.key.get_pressed()
    dx = 0
    dy = 0
    movendo = False

    if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
        dx = -VELOCIDADE
        direcao = 'esquerda'
        movendo = True
    elif teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
        dx = VELOCIDADE
        direcao = 'direita'
        movendo = True

    if teclas[pygame.K_UP] or teclas[pygame.K_w]:
        dy = -VELOCIDADE
        direcao = 'cima'
        movendo = True
    elif teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
        dy = VELOCIDADE
        direcao = 'baixo'
        movendo = True

    jogador.x += dx
    colidiu, rect_tile = verificar_colisao(jogador, grade, tiles_solidos)
    if colidiu:
        if dx > 0:
            jogador.right = rect_tile.left
        else:
            jogador.left = rect_tile.right

    jogador.y += dy
    colidiu, rect_tile = verificar_colisao(jogador, grade, tiles_solidos)
    if colidiu:
        if dy > 0:
            jogador.bottom = rect_tile.top
        else:
            jogador.top = rect_tile.bottom

    if movendo:
        timer_anim += dt
        if timer_anim >= 100:
            timer_anim = 0
            frame_atual = (frame_atual + 1) % 4
    else:
        frame_atual = 0
        timer_anim = 0

    cam_x = jogador.centerx - LARGURA // 2
    cam_y = jogador.centery - ALTURA // 2

    cam_x = max(0, min(cam_x, LARGURA_MAPA - LARGURA))
    cam_y = max(0, min(cam_y, ALTURA_MAPA - ALTURA))

    tela.fill((10, 8, 15))

    for linha in range(len(grade)):
        for coluna in range(len(grade[linha])):
            id_tile = grade[linha][coluna]
            superficie = mapa_tiles[id_tile]
            x = coluna * TAMANHO_TILE - cam_x
            y = linha * TAMANHO_TILE - cam_y
            tela.blit(superficie, (x, y))

    img_frame = frames_jogador[direcao][frame_atual]
    tela.blit(img_frame, (jogador.x - cam_x, jogador.y - cam_y))

    pygame.display.flip()

pygame.quit()
sys.exit()
