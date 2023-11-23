import pygame
from pygame.sprite import Group

def run_game():
 ship = Ship(ai_settings, screen)
 bullets = Group()
 while True:
    gf.check_events(ai_settings, screen, ship, bullets)
    ship.update()