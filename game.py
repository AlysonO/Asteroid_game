# %%
import pygame

from utils import load_sprite
from models import Spaceship

running = True

class Asteroids:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("backgroundsakura", False)
        self.clock = pygame.time.Clock()
        self.spaceship = Spaceship((400, 300))

    def main_loop(self):
        while running:
            self._handle_input()
            self._game_logic()
            self._graphics()

    def _init_game(self):
        pygame.init()
        pygame.display.set_caption("Sakura Rain")

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()

        is_key_pressed = pygame.key.get_pressed()

        if is_key_pressed[pygame.K_RIGHT]:
            self.spaceship.rotate(clockwise=True)
        elif is_key_pressed[pygame.K_LEFT]:
            self.spaceship.rotate(clockwise=False)
        if is_key_pressed[pygame.K_UP]:
            self.spaceship.accelerate()

    def _game_logic(self):
        self.spaceship.move(self.screen)

    def _graphics(self):
        self.screen.blit(self.background, (0, 0))
        self.spaceship.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(30)

