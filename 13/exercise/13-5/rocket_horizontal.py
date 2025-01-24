import pygame
import sys

from settings import Settings
from bullet import Bullet
from ship import Ship

class Rocket_horizontal:
    """管理游戏资源和类的行为"""
    def __init__(self):
        """初始化游戏的资源"""
        pygame.init()
        self.clock=pygame.time.Clock()
        self.settings=Settings()
        #屏幕设置
        self.screen=pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))
        #创建窗口名称
        pygame.display.set_caption("rocket horizontal")

        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()
        self.aliens=pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """相应按键鼠标事件"""
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type==pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        """相应按下"""
        if event.key==pygame.K_UP:
            self.ship.moving_up=True
        elif event.key==pygame.K_DOWN:
            self.ship.moving_down=True
        elif event.key==pygame.K_q:
            sys.exit()
        elif event.key==pygame.K_SPACE:
            print("Space pressed!")
            self._fire_bullet()

    def _check_keyup_events(self,event):
        """相应释放"""
        if event.key==pygame.K_UP:
            self.ship.moving_up=False
        if event.key==pygame.K_DOWN:
            self.ship.moving_down=False

    def _fire_bullet(self):
        """创建子弹并加入编组"""
        if len(self.bullets)<self.settings.bullet_allowed:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)
            print("Bullet fired!")

    def _update_bullets(self):
        """更新子弹的纸质并删除已经消失的子弹"""
        #更新子弹的位置
        self.bullets.update()

        #删除已经消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.left >=1200:
                self.bullets.remove(bullet)
        print(len(self.bullets))

    def _update_aliens(self):
        """更新外星人的位置"""
        self._check_fleet_edges()
        self.aliens.update()

    def _create_fleet(self):
        """创建外星人舰队"""
        #创建一个外星人舰队,不断添加,

    def _update_screen(self):
        """更新屏幕上的图像"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        #将画面显示到屏幕
        pygame.display.flip()

if __name__=='__main__':
    #创建游戏实例并运行
    ai=Rocket_horizontal()
    ai.run_game()                