import pygame
import sys
from pygame.sprite import Sprite

class Settings:
    def __init__(self):
        #屏幕设置
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(0,30,130)

        #雨滴设置
        self.raindrop_speed=1.0
        self.raindrop_width=1
        self.raindrop_height=5
        self.raindrop_color=(160,160,255)

        #雨滴速度设置
        self.raindrop_speed=1.0
        self.raindrop_drop_speed=1
        #方向数值1为向右,-1为向左
        self.raindrops_direction=1

class Raindrop(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.color=self.settings.raindrop_color

        self.rect=pygame.Rect(0,0,self.settings.raindrop_width,
                              self.settings.raindrop_height)
        #放在左上角附件,注意使用的是自己的坐标
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        self.x=float(self.rect.x)

    def check_edges(self):
        """触碰到边缘返回Ture"""
        screen_rect=self.screen.get_rect()
        return (self.rect.right>=screen_rect.right)or (self.rect.left>=0)
    
    def update(self):
        self.x+=self.settings.raindrop_speed*self.settings.raindrops_direction
        self.rect.x=self.x

    def draw_raindrop(self):
        pygame.draw.rect(self.screen,self.color,self.rect)

class Run:
    def __init__(self):
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()

        self.screen=pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height)
        )
        pygame.display.set_caption("Raindrop")

        self.raindrops=pygame.sprite.Group()

        self._create_raindrops()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self._update_raindrops()
            self._update_screen()
            self.clock.tick(60)

    def _update_raindrops(self):
        self._check_raindrops_edges()
        self.raindrops.update()

    def _create_raindrops(self):
        raindrop=Raindrop(self)
        raindrop_width,raindrop_height=raindrop.rect.size

        current_x,current_y=raindrop_width+10,raindrop_height
        while current_y<(self.settings.screen_height-2*raindrop_height):
            while current_x<(self.settings.screen_width-2*raindrop_width):
                self._create_raindrop(current_x,current_y)
                current_x+=10*raindrop_width
            current_x=raindrop_width+10
            current_y+=5*raindrop_height

    def _create_raindrop(self,x,y):
        """创建新的雨滴"""
        new_raindrop=Raindrop(self)
        new_raindrop.x=x
        new_raindrop.rect.x=x
        new_raindrop.rect.y=y
        self.raindrops.add(new_raindrop)

    def _check_raindrops_edges(self):
        for raindrop in self.raindrops.sprites():
            if raindrop.check_edges():
                self._chage_raindrops_direction()
                break

    def _chage_raindrops_direction(self):
        for raindrop in self.raindrops.sprites():
            raindrop.rect.y+=self.settings.raindrop_drop_speed
        self.settings.raindrops_direction*=-1

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for raindrop in self.raindrops.sprites():
            raindrop.draw_raindrop()

        pygame.display.flip()

if __name__ == '__main__':
    ai=Run()
    ai.run_game()
