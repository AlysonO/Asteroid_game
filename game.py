# %%
import pygame
from utils import load_sprite

running = True

class Asteroids:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("backgroundsakura", False)

    def main_loop(self):
        while running:
            self._handle_input()
            self._game_logic()
            self._graphics()

    def _init_game(self):
        pygame.init()
        pygame.display.set_caption("Asteroids")

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()

    def _game_logic(self):
        pass

    def _graphics(self):
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

