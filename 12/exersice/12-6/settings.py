class Settings:
    """存储所有类的设置"""
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(30,30,30)

        #飞船设置
        self.ship_speed=1

        #子弹设置
        self.bullet_speed=3
        self.bullet_width=15
        self.bullet_height=3
        self.bullet_color=(30,30,250)
        self.bullet_allowed=3