import sys
import time

import pygame

from alien import AlienGenerator
from config import *
from spaceship import SpaceshipGenerator


class PySpaceInvaders:

    def __init__(self):
        pygame.init()
        self.window_surface = pygame.display.set_mode(WINDOW_SIZE)

        self.spaceship = SpaceshipGenerator.generate()
        self.aliens = AlienGenerator.generate()

        self.last_update_time = None
        self.last_draw_time = None

    def play(self):

        self.last_update_time = self._time_ms()
        self.last_draw_time = self._time_ms()

        while True:
            self.update()
            self.draw()

    def get_events(self):
        events = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            events.append(event)
        return events

    def update(self):
        elapsed_time_ms = self._time_ms() - self.last_update_time
        if elapsed_time_ms < UPDATE_PERIOD_MS:
            return

        events = self.get_events()

        if self.spaceship: self.spaceship.update(elapsed_time_ms, events)
        self.aliens.update(elapsed_time_ms)

        self.collide()

        self.last_update_time += elapsed_time_ms

    def draw(self):

        elapsed_time_ms = self._time_ms() - self.last_draw_time
        if elapsed_time_ms < DRAW_PERIOD_MS:
            return

        self.window_surface.fill((0, 0, 0,))

        if self.spaceship:  self.spaceship.draw(self.window_surface)
        self.aliens.draw(self.window_surface)

        pygame.display.flip()

        self.last_draw_time += elapsed_time_ms

    def _time_ms(self):
        return time.time_ns() // 1000000

    def collide(self):
        self._collide_missile_and_aliens()
        self._collide_spaceship_and_aliens()

    def _collide_missile_and_aliens(self):
        if self.spaceship is None or self.spaceship.missile is None:
            return
        missile_rect = self.spaceship.missile.rect
        for alien in self.aliens:
            if missile_rect.colliderect(alien.rect):
                self.aliens.remove(alien)
                self.spaceship.missile = None

    def _collide_spaceship_and_aliens(self):
        for alien in self.aliens:

            if self.spaceship is None:
                return

            if alien.rect.colliderect(self.spaceship.rect):
                self.spaceship = None


if __name__ == "__main__":
    game = PySpaceInvaders()
    game.play()