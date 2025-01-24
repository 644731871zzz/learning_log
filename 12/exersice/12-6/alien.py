import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """创建新的外星人组"""
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.screen_rect=ai_game.screen

        self.image=pygame.image.load('')
