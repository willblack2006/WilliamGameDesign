import pygame,time
pygame.init()

wind=pygame.display.set_mode((700,700))
pygame.display.set_caption("Testing")

#create different fonts

TITLE_FNT=pygame.font.SysFont('comicsans',80)
MENU_FNT=pygame.font.SysFont('comicsans',40)
INST_FNT=pygame.font.SysFont('comicsans',15)

text=TITLE_FNT.render('Welcome!',1,(255,255,255))
wind.fill((0,0,0))
wind.blit(text,(170,50))

text=MENU_FNT.render('Instructions',0.5,(255,255,255))
wind.blit(text,(95,160))

text=INST_FNT.render('Press W to move up, A to move left, S to move down, and D to move right',.5,(255,255,255))
wind.blit(text,(110,220))

text=INST_FNT.render('Navigate the circle to hit the square in order to grow!',.5,(255,255,255))
wind.blit(text,(110,240))

pygame.display.update()
pygame.time.delay(10000)
