import pygame
import sys
from pygame.sprite import Sprite
from random import randint

class Settings:
    def __init__(self):
        #屏幕设置
        self.screen_width=1350
        self.screen_height=950
        self.bg_color=(0,30,130)

        #雨滴设置
        self.raindrop_width=3
        self.raindrop_height=12
        self.raindrop_color=(130,130,255)

        #雨滴下落速度 
        self.raindrop_speed_y=3
        #雨滴左右横移速度
        self.raindrop_speed_x=1

class Raindrop(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.color=self.settings.raindrop_color

        #雨滴位置初始化
        self.rect=pygame.Rect(0,0,self.settings.raindrop_width,
                              self.settings.raindrop_height)
        #在屏幕上方绘制
        self.rect.x=randint(0,self.settings.screen_width)
        self.rect.y=-50

        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
    
    def update(self):
        """更新雨滴位置"""
        self.y+=self.settings.raindrop_speed_y
        self.x+=randint(-self.settings.raindrop_speed_x,
                        self.settings.raindrop_speed_x)
        self.rect.y=self.y
        #配置x保证雨滴不会超出左右边界
        self.rect.x=max(0,min(self.x,self.settings.screen_width))

    def draw_raindrop(self):
        """绘制雨滴"""
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



    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self._update_raindrops()
            self._create_raindrops()
            self._update_screen()
            self.clock.tick(60)

    def _update_raindrops(self):
        """更新雨滴位置并删除超过屏幕的雨滴"""
        self.raindrops.update()

        #删除超出屏幕的雨滴
        for raindrop in self.raindrops.sprites():
            if raindrop.rect.top>=self.settings.screen_height:
                self.raindrops.remove(raindrop)

    def _create_raindrops(self):
        """随机生成新的雨滴"""
        new_raindrop=Raindrop(self)
        self.raindrops.add(new_raindrop)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for raindrop in self.raindrops.sprites():
            raindrop.draw_raindrop()

        pygame.display.flip()

if __name__ == '__main__':
    ai=Run()
    ai.run_game()
