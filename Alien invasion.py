import sys

import pygame
from pygame.Sprite import Group
from alien import Alien
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
import game_function as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    #Set the BG color
    bg_color = (230, 230, 230)
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, "Play")
    ship = Ship(ai_settings, screen)
    bullets = Group()
    alien = Group()
    stats = GameStats(ai_settings)
    # Start the main loop of the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)
        gf.create_fleet(ai_settings, screen, ship, alien, bullets)
        bullets.update()
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets,
                         play_button)
run_game()