import pygame

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
VELOCIDADE = 1
RAIO = 30
pygame.init()

tela = pygame.display.set_mode((640, 480), 0)
x = 10 # posição inicial do eixo x
y = 10 # posição inicial do eixo y
vel_x = VELOCIDADE
vel_y = VELOCIDADE
while True:
    # calcula as regras
    x += vel_x # incrementa ou decrementa para que a bola saia do lugar
    y += vel_y
    if x + RAIO > 640:
        vel_x = -VELOCIDADE
    if x - RAIO < 0:
        vel_x = VELOCIDADE

    if y + RAIO > 480:
        vel_y = -VELOCIDADE
    if y - RAIO < 0:
        vel_y = VELOCIDADE
    # pinta
    tela.fill(PRETO) # pinta de preto, apagando o rastro da bola
    pygame.draw.circle(tela, AMARELO, (int(x), int(y)), RAIO, 0) # (<surface>, <cor>, <ponto_central>, <raio>, <espessura>)
    pygame.display.update()
    # eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()