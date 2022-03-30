#will black
#make main menu
#width/height of text, mouse position
#variables, constants, and objects

import pygame, time, os
os.system('cls')
pygame.init()

#color dictionary
colors={'red':[255,0,0],'white':[255,255,255],'mag':[255,0,255],
'aqua':[51,153,255],'m':[47,192,229], 'navy':[5,31,64]}


#variables
WIDTH=700
HEIGHT=700
xs=20
ys=120
wb=40
hb=25
yT=10
square=pygame.rect(xs,ys,wb,hb)

#variable's colors
sq_color=colors.get('mag')
title_color=colors.get('navy')
background=colors.get('white')

#fonts
TITLE_FNT=pygame.font.SysFont('comicsans',80)
MENU_FNT=pygame.font.SysFont('comicsans',40)
INST_FNT=pygame.font.SysFont('comicsans',15)

#list of menu titles
message=''
mainmenu=['Instructions','Settings','Level 1','Level 2','Level 3','Scoreboard','Exit']

#create screen (caption is what is at the top of window)
window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Circle Vs. Square')

#title text
title=TITLE_FNT.render('MENU',1,title_color)
xT=WIDTH/2-title.get_width()/2
window.fill(background)
window.blit(title(xT,yT))

#create menu loop
for message in mainmenu:  
    pygame.draw.rect(window,sq_color,square)

    #menu text
    text=MENU_FNT.render(message,1,title_color)
    window.blit(text,(square.x+wb+10,square.y-5))
    square.y+=75

#mouse click check
check=True
while check:
    window.fill(background)
    move=10
    for case in pygame.event.get():
        if case.type==pygame.QUIT:
            check=False
    if case.type==pygame.MOUSEBUTTONDOWN:
        mouse_pos=pygame.mouse.get_pos()
    if (mouse_pos[0]>=20 and mouse_pos[0]<60) and (mouse_pos[1]>=120 and mouse_pos[1]<=160):
        window.fill(background)
    



pygame.display.update()
pygame.time.delay(1000)