import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """创建并管理子弹类"""

    def __init__(self,ai_game):

        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.color=self.settings.bullet_color

        #在(0,0)处先创建一个子弹,再更新到正确的位置
        self.rect=pygame.Rect(0,0,self.settings.bullet_width,
                              self.settings.bullet_height)
        self.rect.midright=ai_game.ship.rect.midright
        
        #用浮点存储子弹的位置
        self.x=float(self.rect.x)

    def update(self):
        """向右移动子弹"""
        #更新子弹的准确位置
        self.x+=self.settings.bullet_speed
        #表示子弹的新的位置
        self.rect.x=self.x

    def draw_bullet(self):
        """绘制子弹的位置"""
        print(f"Drawing bullet at {self.rect.x}, {self.rect.y}")
        pygame.draw.rect(self.screen,self.color,self.rect)