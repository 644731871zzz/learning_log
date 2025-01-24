import pygame
import sys
from pygame.sprite import Sprite

class Settings:
    def __init__(self):
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(0,30,60)

class Star(Sprite):
    def __init__(self,run_star):
        super().__init__()
        self.screen=run_star.screen
        self.image=pygame.image.load('image/star.bmp')
        self.rect=self.image.get_rect()
        
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

class Run_star:
    def __init__(self):
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()

        self.screen=pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        
        pygame.display.set_caption("run star")

        self.stars=pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self._update_screen()
            self.clock.tick(60)

    def _create_fleet(self):
        star=Star(self)
        star_width,star_height=star.rect.size
        current_x,current_y=star_width,star_height
        while current_y<self.settings.screen_height-star_height:
            while current_x<self.settings.screen_width-star_width:
                self._creat_alien(current_x,current_y)
                current_x+=2*star_width
            current_x=star_width
            current_y+=2*star_height

    def _creat_alien(self,x_star,y_star):
        new_star=Star(self)
        new_star.rect.x=x_star
        new_star.rect.y=y_star
        self.stars.add(new_star)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        pygame.display.flip()

if __name__=='__main__':
    ai=Run_star()
    ai.run_game()



        