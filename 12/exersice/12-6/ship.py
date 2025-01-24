import pygame

class Ship:
    """创建并存储一个飞创的所需要的东西 管理飞船的类"""

    def __init__(self,ai_game):
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.screen_rect=ai_game.screen.get_rect()

        #加载飞船图像并获取外接矩形
        self.image=pygame.image.load('image/ship.bmp')
        self.rect=self.image.get_rect()

        #每艘飞船放在屏幕的左侧中间位置
        self.rect.midleft=self.screen_rect.midleft

        #将y数据存储为浮点数
        self.y=float(self.rect.y)

        #移动标志,但是一开始并不移动
        self.moving_up=False
        self.moving_down=False

    def update(self):
        """根据移动调整飞船的位置"""
        if self.moving_up and self.rect.top>self.screen_rect.top:
            self.y-=self.settings.ship_speed
        if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
            self.y+=self.settings.ship_speed

        #根据self.y更新rect中的y
        self.rect.y=self.y

    def blitme(self):
        """指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)


