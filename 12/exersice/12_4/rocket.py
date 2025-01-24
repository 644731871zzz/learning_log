import pygame
import sys


class Settings:
    """管理游戏中的设置类"""
    def __init__(self):
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)

        self.rocket_speed=1.5

class Ship:
    def __init__(self,ai_game):
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.screen_rect=ai_game.screen.get_rect()

        self.image=pygame.image.load('rocket.bmp')
        self.rect=self.image.get_rect()

        self.rect.midbottom=self.screen_rect.midbottom

        self.x=float(self.rect.x)
        
        self.moving_right=False
        self.moving_left=False

    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x+=self.settings.rocket_speed
        if self.moving_left and self.rect.left>0:
            self.x-=self.settings.rocket_speed
        
        self.rect.x=self.x

    def blitme(self):
        self.screen.blit(self.image,self.rect)


class Rocket:
    """管理游戏资源的类"""
    def __init__(self):
        """初始化游戏资源"""
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()

        self.screen=pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("rocket_move")

        self.ship=Ship(self)

    def run_game(self):
        """开始游戏主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        """响应按键和鼠标的事件"""
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==pygame.KEYDOWN:
                self._check_keydown_events(event)
            if event.type==pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=True
        if event.key==pygame.K_LEFT:
            self.ship.moving_left=True
        if event.key==pygame.K_q:
            sys.exit()
    
    def _check_keyup_events(self,event):
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=False
        if event.key==pygame.K_LEFT:
            self.ship.moving_left=False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()
    

if __name__=='__main__':
    ai=Rocket()
    ai.run_game()