import pygame
import sys

class Settings:
    def __init__(self):
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(230,230,230)



class Key:
    def __init__(self):
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()

        self.screen=pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("keydown")
    
    def run_game(self):
        while True:
            self._check_event()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_event(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==pygame.KEYDOWN:
                self._check_keydown(event)

    def _check_keydown(self,event):
        print(f"keydown {event.key}")

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()

if __name__ == '__main__':
    ai=Key()
    ai.run_game()

