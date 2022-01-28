from game import *

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

def handling_input():
    global mon_dy, mon_dx, index
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