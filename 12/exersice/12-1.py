import pygame
import sys

pygame.init()

screen_width=1000
screen_height=750
screen_bg_color=(50,50,220)

screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("12-1")

image=pygame.image.load('sam.bmp')
screen_rect=screen.get_rect()
image_rect=image.get_rect()

image_rect.midbottom=screen_rect.midbottom




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(screen_bg_color)
    screen.blit(image,image_rect)
    pygame.display.flip()


