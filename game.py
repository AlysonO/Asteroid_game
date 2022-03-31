# %%
import pygame

from utils import load_sprite, get_random_position
from models import Spaceship, Asteroid

running = True

class Asteroids:
    MIN_ASTEROID_DISTANCE = 250

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("backgroundsakura", False)
        self.clock = pygame.time.Clock()

        self.asteroids = []
        self.spaceship = Spaceship((400, 300))

        for _ in range(6):
            while True:
                position = get_random_position(self.screen)
                if (position.distance_to(self.spaceship.position) > self.MIN_ASTEROID_DISTANCE):
                    break
            self.asteroids.append(Asteroid(position))

    def main_loop(self):
        while running:
            self._handle_input()
            self._game_logic()
            self._graphics()

    def _init_game(self):
        pygame.init()
        pygame.display.set_caption("Sakura Rain")

    def _get_game_objects(self):
        game_objects = [*self.asteroids]

        if self.spaceship:
            game_objects.append(self.spaceship)

        return game_objects

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()

        is_key_pressed = pygame.key.get_pressed()

        if self.spaceship:
            if is_key_pressed[pygame.K_RIGHT]:
                self.spaceship.rotate(clockwise=True)
            elif is_key_pressed[pygame.K_LEFT]:
                self.spaceship.rotate(clockwise=False)
            if is_key_pressed[pygame.K_UP]:
                self.spaceship.accelerate()

    def _game_logic(self):
        for game_object in self._get_game_objects():
            game_object.move(self.screen)

        if self.spaceship:
            for asteroid in self.asteroids:
                if asteroid.collides_with(self.spaceship):
                    self.spaceship = None
                    break

    def _graphics(self):
        self.screen.blit(self.background, (0, 0))

        for game_object in self._get_game_objects():
            game_object.draw(self.screen)

        pygame.display.flip()
        self.clock.tick(30)



