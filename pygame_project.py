# %%

import pygame


successes, failures = pygame.init()

screen_width = 720
screen_height = 480

screen = pygame.display.set_mode((screen_width, screen_height))  
clock = pygame.time.Clock()
FPS = 60
clock.tick(FPS)

running = True
mon_rect = pygame.rect.Rect(10, 10, 20, 30)
mon_x = 10
mon_y = 10
mon_dx = 0 #dérivée de x par rapport au temps (don't ask me, i don't know)
mon_dy = 0

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
index = 0

def check_limits():
    global mon_x, mon_y
    if mon_x > screen_width-20:
        mon_x = screen_width-20
    else: 
        mon_x += mon_dx * mon_delai
    if mon_y > screen_height-30:
        mon_y = screen_height-30
    else: 
        mon_y += mon_dy * mon_delai

    if mon_x < 0:
        mon_x = 0
    else: 
        mon_x += mon_dx * mon_delai
    if mon_y < 0:
        mon_y = 0
    else: 
        mon_y += mon_dy * mon_delai
    return 0




while running:

    mon_delai = clock.tick(FPS) / 1000

    screen.fill((0, 0, 0))

    check_limits()

    mon_rect.left = mon_x
    mon_rect.top = mon_y
    color = colors[index]
    pygame.draw.rect(screen, color, mon_rect)
    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            index += 1
            index %= len(colors)
            color = colors[index]

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                mon_dx += 60
            if event.key == pygame.K_LEFT:
                mon_dx -= 60
            if event.key == pygame.K_DOWN:
                mon_dy += 60
            if event.key == pygame.K_UP:
                mon_dy -= 60

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                mon_dx -= 60
            if event.key == pygame.K_LEFT:
                mon_dx += 60
            if event.key == pygame.K_DOWN:
                mon_dy -= 60
            if event.key == pygame.K_UP:
                mon_dy += 60


pygame.quit()
# %%
