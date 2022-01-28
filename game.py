import pygame
from input_handling import check_limits, handling_input
from game_elements import draw_player

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
mon_delai = clock.tick(FPS) / 1000

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
index = 0
color = colors[index]
# %%
def __main__():
    while running:
        screen.fill((0, 0, 0))

    
        draw_player()
        check_limits()
        handling_input()


pygame.quit()
# %%