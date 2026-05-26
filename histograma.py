import pygame, sys
import random
from pygame.locals import QUIT

pygame.init()

screen = pygame.display.set_mode((1200, 700))

fonte = pygame.font.SysFont("Arial", 16)

def contabiliza_totais(nums, num_cat):

    num_min = min(nums)
    num_max = max(nums)

    tam_cat = (num_max - num_min) / num_cat

    lista_total = [0] * num_cat

    for num in nums:

        if num == num_max:
            lista_total[-1] += 1
            continue

        for i_cat in range(num_cat):

            lim_inf = num_min + i_cat * tam_cat
            lim_sup = lim_inf + tam_cat

            if lim_inf <= num < lim_sup:
                lista_total[i_cat] += 1
                break

    return lista_total, num_min, num_max, tam_cat


def desenha_histograma(screen, nums, num_cat, x_inicial, titulo, cores):

    lista_total, num_min, num_max, tam_cat = contabiliza_totais(nums, num_cat)

    eixo_x = x_inicial
    eixo_y = 550

    largura_barra = 35
    espacamento = 15

    altura_max = 250

    maior_frequencia = max(lista_total)

    texto_titulo = fonte.render(titulo, True, (255, 255, 255))
    screen.blit(texto_titulo, (x_inicial, 50))

    # eixo y
    pygame.draw.line(screen, (255, 255, 255), (eixo_x, eixo_y - altura_max), (eixo_x, eixo_y), 3)

    # eixo x
    pygame.draw.line(screen, (255, 255, 255), (eixo_x, eixo_y), (eixo_x + 300, eixo_y), 3)

    for i in range(maior_frequencia + 1):

        y = eixo_y - (i / maior_frequencia) * altura_max

        pygame.draw.line(screen, (200, 200, 200), (eixo_x - 5, y), (eixo_x + 5, y), 2)

        texto = fonte.render(str(i), True, (255, 255, 255))
        screen.blit(texto, (eixo_x - 25, y - 10))

    for i in range(num_cat):

        freq = lista_total[i]

        altura = (freq / maior_frequencia) * altura_max

        x = eixo_x + 20 + i * (largura_barra + espacamento)

        y = eixo_y - altura

        pygame.draw.rect(
            screen,
            cores[i],
            (x, y, largura_barra, altura)
        )

        texto_freq = fonte.render(str(freq), True, (255, 255, 255))
        screen.blit(texto_freq, (x + 5, y - 20))

        lim_inf = int(num_min + i * tam_cat)
        lim_sup = int(lim_inf + tam_cat)

        texto_faixa = fonte.render(
            f"{lim_inf}-{lim_sup}",
            True,
            (255, 255, 255)
        )

        screen.blit(texto_faixa, (x - 10, eixo_y + 10))

# histograma 1
lista1 = []

for _ in range(50):
    lista1.append(random.randint(0, 100))

categorias1 = 5

# histograma 2
lista_base = [10, 20, 30, 40, 50]

lista2 = []

for valor in lista_base:

    quantidade = random.randint(1, 5)

    for _ in range(quantidade):
        lista2.append(valor)

categorias2 = 3


# histograma 3
lista3 = []

print("\nDigite 5 números para o terceiro histograma:\n")

for i in range(5):

    num = int(input(f"Número {i+1}: "))
    lista3.append(num)

categorias3 = 6

cores1 = []

for _ in range(categorias1):
    cores1.append((
        random.randint(50,255),
        random.randint(50,255),
        random.randint(50,255)
    ))

cores2 = []
for _ in range(categorias2):
    cores2.append((
        random.randint(50,255),
        random.randint(50,255),
        random.randint(50,255)
    ))

cores3 = []
for _ in range(categorias3):
    cores3.append((
        random.randint(50,255),
        random.randint(50,255),
        random.randint(50,255)
    ))
    
while True:

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30, 30, 30))

    desenha_histograma(screen, lista1, categorias1, 50, "Histograma 1", cores1)

    desenha_histograma(screen, lista2, categorias2, 430, "Histograma 2", cores2)

    desenha_histograma(screen, lista3, categorias3, 800, "Histograma 3", cores3)

    pygame.display.update()