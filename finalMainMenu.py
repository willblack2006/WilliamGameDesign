#William Black
#5/9/22
#make a pacman like game, move thing around screen, how to draw shape, how to use keys to move objects, dictionary
#objective of game: rectange to run away from circle;if the 2 collide, rect disappears and circle gets bigger
from decimal import ROUND_UP

import os, random, math,datetime
import pygame as p
from pygame.locals import *
        
os.system('cls')

name= input("What is your name?  ")
#intailize p
p.init()

#MENU VARIABLES
WIDTH=700
HEIGHT=700
xs=50
ys=250
wb=30
hb=30
#declare constants
MAIN=True
INSTR=False
SETT=False
BACKCLR=False
CRCLR=False
SIZE=False
LEV_1=False
LEV_2=False
LEV_3=False
PSCORE1=False
SCOREBOARD=False
EXIT=False
#lists fr messages
MenuList=["Instructions", 'Settings', 'Play Platformer',  "Scoreboard", "Exit"]
SettingList=[ 'Background Color', 'Circle Color','Screen size']
BackColorList=['Aqua',"Magenta", "Yellow", "Orange"]
CrClrList=['Green', "White", "Lilac", "Navy"]
SizeList=['800x800', '1000x1000','Orginal']
#screen
screen=p.display.set_mode((WIDTH,HEIGHT))

#Fonts
TITLE_FNT= p.font.SysFont("timesnewroman", 80)
SUBT_FNT= p.font.SysFont("comicsans", 40)
MENU_FNT= p.font.SysFont("arial", 50)
INST_FNT= p.font.SysFont('comicsans', 30)
#THE GAME VARIABLES
#declare consants,variables, lists and dictionary
check=True
move=5
grow=5
eaten=0
sec=0
#squareG variables
xsg=20
ysg=20
wbox=30
hbox=30
#circle variables
rad=15
xc=random.randint(rad, WIDTH-rad)
yc=random.randint(rad, HEIGHT-rad)
#inner box
ibox=rad*math.sqrt(2)
xig= xc-(ibox/2)
yig= yc-(ibox/2)
inscribSq=p.Rect(xig,yig,ibox,ibox)
#create the rect object
squareG=p.Rect(xsg, ysg, wbox, hbox)
square=p.Rect(xs,ys,wb,hb)
#Define Colors
colors={'white': [255,255,255], 'red': [255,0,0], 'orange':[255, 85, 0], 'navy':[5, 31, 64], 
'forest':[16, 46, 12],'aqua':[51, 153, 255], 'pink': [200,75,125], 'litpur':[203,160,227],
'mag':[255, 0, 255], 'yellow':[240, 180, 14] }
#Get colors
background=colors.get('white')
sq_color=colors.get('navy')
cr_color=colors.get('')
inscribSq_color=colors.get('white')
sqM_color=colors.get('navy')
#GLobalization setup
txt=''
txty=''
xt=''
def TitleMenu(message):
    txt=TITLE_FNT.render(message, 1, (0, 0,0))
    screen.fill((background))
    #get width of the text
    #x value = WIDTH/2 - wtext
    xt= WIDTH/2-txt.get_width()/2
    screen.blit(txt,(xt,50))

def ReturnBut(message):
    txt=MENU_FNT.render(message, 1, (255, 255, 255))
    xt= WIDTH/2-txt.get_width()/2
    screen.blit(txt,(xt,550))
    
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier
# got this from https://realpython.com/python-rounding/#rounding-up
#this function uses parameters fr menu
def mainmenu(Mlist):
    txty=245
    square.y=250
    for i in range(len(Mlist)):
        message=Mlist[i]
        txt=INST_FNT.render(message, 1, (5, 31, 64) )
        screen.blit(txt, (90,txty))
        txty+=50
        p.draw.rect(screen, sqM_color, square)
        square.y+=50
  
def instr(): 
     
    txt=INST_FNT.render("Control your character with the arrow keys.", 1,(5, 31, 64))
    xt= WIDTH/2-txt.get_width()/2
    screen.blit(txt,(xt,200))
    txt=INST_FNT.render("Jump with the space bar", 1, (5, 31, 64)) 
    screen.blit(txt,(xt,240))
    txt=INST_FNT.render("Jump to each platform until the door.h",1, (5, 31, 64))
    screen.blit(txt, (xt,280))
    txt=INST_FNT.render("Keep playing until you finish!",1, (5, 31, 64))
    screen.blit(txt, (xt,320)) 


def keepScore(score):
    date=datetime.datetime.now()
    print(date.strftime('%m/%d/%Y'))
    scoreLine=str(score)+"\t"+name+"\t"+date.strftime('%m/%d/%Y'+'\n')
    print (scoreLine)
    #open file and write in it
    myFile=open('Class Stuff\CircleEatsSquare\ScrBrd.txt', 'a')
    myFile.write(scoreLine)
    myFile.close()

def scoreb():
    myFile=open('Class Stuff\CircleEatsSquare\ScrBrd.txt', 'r')
    yi=150
    stuff= myFile.readlines()
    myFile.close()
    stuff.sort(reverse=True)

    for i in stuff[0:5]:
        txt=INST_FNT.render(i,1,"navy")
        xt= WIDTH/2-txt.get_width()/2
        screen.blit(txt, (xt,yi))
        yi+=50

def changeClr():
    global randColor
    colorCheck=True
    while colorCheck:
        randColor=random.choice(list(colors))
        if colors.get(randColor) == background:
            randColor=random.choice(list(colors))
        else:
            colorCheck=False
changeClr()
sq_color=colors.get(randColor)  

def changeScreenSize(xm,ym):
    global HEIGHT, WIDTH, screen
    if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290)):
        HEIGHT=800
        WIDTH=800
        print('here!')

    if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <340)):
        HEIGHT=1000
        WIDTH=1000
        
    if ((mouse_pos[0] >0 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <390)):
        HEIGHT=700
        WIDTH=700
    screen=p.display.set_mode((WIDTH,HEIGHT))

######################################################################################################################
MAX=10
jumpCount=10
JUMP=False
mouse_pos=(0,0)
xm= mouse_pos[0]
ym=mouse_pos[1]
while check:
    keys=p.key.get_pressed()
    if MAIN:
        screen.fill(background)
        TitleMenu("Platformer")
        mainmenu(MenuList)
    if INSTR:
        screen.fill(background)
        TitleMenu("Instructions")
        ReturnBut("Return to Menu")
        instr()
    if SETT: 
        screen.fill(background)
        TitleMenu("Settings")
        ReturnBut("Return to Menu")
        mainmenu(SettingList)   
    if BACKCLR:
        screen.fill(background)
        TitleMenu("Background Color")
        ReturnBut("Back")
        mainmenu(BackColorList)   
    if CRCLR:
        screen.fill(background)
        TitleMenu("Circle Color")
        ReturnBut("Back")
        mainmenu(CrClrList)
    if SIZE:
        screen.fill(background)
        TitleMenu("Screen Size")
        ReturnBut("Back")
        mainmenu(SizeList)     
    if PSCORE1:
        timePlayed=((ticksEnd/1000)-(ticksStart/1000))
        timePlyR=round_up(timePlayed)
        screen.fill(background)
        TitleMenu("Your Score")
        ReturnBut("Return to Menu")
        txt=INST_FNT.render("Your score is:", 1,(5, 31, 64))
        xt= WIDTH/2-txt.get_width()/2
        screen.blit(txt,(xt,200))
        score= ((eaten)*5-2*(timePlyR))
        txt=SUBT_FNT.render(str(score), 1, (5, 31, 64))
        xt= WIDTH/2-txt.get_width()/2
        screen.blit(txt,(xt,250))       
    if SCOREBOARD:
        screen.fill(background)
        TitleMenu("ScoreBoard") 
        ReturnBut("Return to Menu")
        scoreb()           
    if EXIT:
        screen.fill(background)
        txt=INST_FNT.render("Thank you for Playing", 1,(5, 31, 64))
        screen.blit(txt,(xt,200))
        txt=INST_FNT.render("Play again soon...", 1, (5, 31, 64)) 
        p.time.delay(2000)
        screen.blit(txt,(xt,240))
        p.time.delay(5000)
        p.QUIT    

    for event in p.event.get():
        if event.type == p.QUIT:
            check = False 
    #Mouse Controls
    #Menu Navigation
    if event.type ==p.MOUSEBUTTONDOWN:
        mouse_pos=p.mouse.get_pos()
        print(mouse_pos)
        
        if MAIN:
            eaten=0
            rad=15
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <280))or INSTR:
                MAIN=False
                screen.fill(background)
                INSTR=True
            if((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <330))or SETT:
                MAIN=False 
                SETT=True
                p.time.delay(300)
                mouse_pos=(0,0)    
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <380))or LEV_1:
                MAIN=False
                LEV_1=True
                ticksStart=p.time.get_ticks()
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >400 and mouse_pos[1] <430))or LEV_2:
                MAIN=False
                LEV_2=True
                ticksStart=p.time.get_ticks()
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >450 and mouse_pos[1] <480))or LEV_3:
                MAIN=False
                LEV_3=True
                ticksStart=p.time.get_ticks()
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >500 and mouse_pos[1] <530))or SCOREBOARD:
                MAIN=False
                SCOREBOARD=True
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >550 and mouse_pos[1] <580))or EXIT:
                MAIN=False
                EXIT=True

        if SETT:
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290))or BACKCLR:
                SETT=False
                screen.fill(background)
                BACKCLR=True
                p.time.delay(300)
                mouse_pos=(0,0)
            if((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <340))or CRCLR:
                SETT=False
                CRCLR=True
                p.time.delay(300)
                mouse_pos=(0,0)
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <390)):
                SETT=False
                SIZE=True
                p.time.delay(400)
                mouse_pos=(0,0) 

        if BACKCLR:
            if ((mouse_pos[0] >306 and mouse_pos[0] <393) and (mouse_pos[1] >560 and mouse_pos[1] <595)) or SETT:
                BACKCLR=False
                SETT=True
                p.time.delay(400)
                mouse_pos=(0,0)
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290)):
                background=colors.get('aqua')  
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <340)):
                background=colors.get('mag')     
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <390)):
                background=colors.get('yellow')
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >400 and mouse_pos[1] <440)):
                background=colors.get('orange')   
        
        if CRCLR:

            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >250 and mouse_pos[1] <290)):
                cr_color=colors.get('forest') 
                inscribSq_color=colors.get('forest')  
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >300 and mouse_pos[1] <340)):
                cr_color=colors.get('white') 
                inscribSq_color=colors.get('white')   
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >350 and mouse_pos[1] <390)):
                cr_color=colors.get('litpur')  
                inscribSq_color=colors.get('litpur')  
            if ((mouse_pos[0] >50 and mouse_pos[0] <80) and (mouse_pos[1] >400 and mouse_pos[1] <440)):
                cr_color=colors.get('navy')  
                inscribSq_color=colors.get('navy')  
            if ((mouse_pos[0] >306 and mouse_pos[0] <393) and (mouse_pos[1] >560 and mouse_pos[1] <595)) or SETT:
                CRCLR=False
                SETT=True
                p.time.delay(400)
                mouse_pos=(0,0)
        if SIZE:
            print("i am here!!!")
            changeScreenSize(xm,ym)
            if ((mouse_pos[0] >306 and mouse_pos[0] <393) and (mouse_pos[1] >560 and mouse_pos[1] <595)) or SETT:
                SIZE=False
                SETT=True
                p.time.delay(400)
                mouse_pos=(0,0)
                
        #return to Menu
        if not MAIN and not LEV_1:
            if ((mouse_pos[0] >210 and mouse_pos[0] <490) and (mouse_pos[1] >561 and mouse_pos[1] <595))or MAIN:
                if INSTR:
                    INSTR=False
                    MAIN=True
                if SETT:
                    SETT=False
                    MAIN=True
                if PSCORE1:
                    PSCORE1=False
                    MAIN=True
                    keepScore(score)
                if SCOREBOARD:
                    SCOREBOARD=False
                    MAIN=True

    #THE GAME Level 1
    if LEV_1:
        playgame()

    if LEV_2:        
        screen.fill(background)
        # Game Controls
        #squareG control
        if keys[p.K_a] and squareG.x>=move :
            squareG.x -= move 
        if keys[p.K_d] and squareG.x <=WIDTH-(wbox+move):
            squareG.x += move
        #jumping part
        if not JUMP:
            if keys[p.K_w] and squareG.y>=move:
                squareG.y -= move  
            if keys[p.K_s] and squareG.y<=HEIGHT-(hbox+move):
                squareG.y += move 
            if keys[p.K_SPACE]:
                JUMP=True
        else:
            if jumpCount>=-MAX:
                squareG.y -= jumpCount*abs(jumpCount)/2
                jumpCount-=1
            else:
                jumpCount=MAX
                JUMP=False
        #circle control
        if keys[p.K_LEFT] and xc >=rad+move:
            xc -= move
        if keys[p.K_RIGHT] and xc<=WIDTH-(rad+move):
            xc += move
        if keys[p.K_UP] and yc>=rad+move:
            yc -= move
        if keys[p.K_DOWN] and yc<=HEIGHT-(rad+move):
            yc+= move
        
        checkCollide=squareG.collidepoint((xc,yc))
        if checkCollide:
            squareG.x=random.randint(wbox, WIDTH-wbox)
            squareG.y=random.randint(hbox, HEIGHT-hbox)
            rad+=grow
        ibox=rad*math.sqrt(2)
        xig= xc-(ibox/2)
        yig= yc-(ibox/2)
        inscribSq=p.Rect(xig,yig,ibox,ibox)
        sqCollide=squareG.colliderect((inscribSq))
        if sqCollide:
            squareG.x=random.randint(wbox, WIDTH-wbox)
            squareG.y=random.randint(hbox, HEIGHT-hbox)
            changeClr()
            sq_color=colors.get(randColor)  
            rad+=grow
            eaten+=1
            # secs=Something to track the amount of time played

        p.draw.rect(screen,sq_color, squareG)    
        p.draw.circle(screen,cr_color, (xc,yc), rad)
        p.draw.rect(screen,inscribSq_color, inscribSq)

        if eaten>=20:
            LEV_2=False
            PSCORE1=True
            ticksEnd=p.time.get_ticks()
            print(ticksStart, ticksEnd)
    
    if LEV_3:        
        screen.fill(background)
        # Game Controls
        #squareG control
        if keys[p.K_a] and squareG.x>=move :
            squareG.x -= move 
        if keys[p.K_d] and squareG.x <=WIDTH-(wbox+move):
            squareG.x += move
        #jumping part
        if not JUMP:
            if keys[p.K_w] and squareG.y>=move:
                squareG.y -= move  
            if keys[p.K_s] and squareG.y<=HEIGHT-(hbox+move):
                squareG.y += move 
            if keys[p.K_SPACE]:
                JUMP=True
        else:
            if jumpCount>=-MAX:
                squareG.y -= jumpCount*abs(jumpCount)/2
                jumpCount-=1
            else:
                jumpCount=MAX
                JUMP=False
        #circle control
        if keys[p.K_LEFT] and xc >=rad+move:
            xc -= move
        if keys[p.K_RIGHT] and xc<=WIDTH-(rad+move):
            xc += move
        if keys[p.K_UP] and yc>=rad+move:
            yc -= move
        if keys[p.K_DOWN] and yc<=HEIGHT-(rad+move):
            yc+= move
        
        checkCollide=squareG.collidepoint((xc,yc))
        if checkCollide:
            squareG.x=random.randint(wbox, WIDTH-wbox)
            squareG.y=random.randint(hbox, HEIGHT-hbox)
            rad+=grow
        ibox=rad*math.sqrt(2)
        xig= xc-(ibox/2)
        yig= yc-(ibox/2)
        inscribSq=p.Rect(xig,yig,ibox,ibox)
        sqCollide=squareG.colliderect((inscribSq))
        if sqCollide:
            squareG.x=random.randint(wbox, WIDTH-wbox)
            squareG.y=random.randint(hbox, HEIGHT-hbox)
            changeClr()
            sq_color=colors.get(randColor)  
            rad+=grow
            eaten+=1
            # secs=Something to track the amount of time played
      
        p.draw.rect(screen,sq_color, squareG)    
        p.draw.circle(screen,cr_color, (xc,yc), rad)
        p.draw.rect(screen,inscribSq_color, inscribSq)

        if eaten>=30:
            LEV_3=False
            PSCORE1=True
            ticksEnd=p.time.get_ticks()
            print(ticksStart, ticksEnd)  
        
    p.display.update()
    p.time.delay(9)


    def playgame():
        from gzip import BadGzipFile
        import pygame
        from pygame import mixer
        import pickle
        from os import path
        import random

        pygame.mixer.pre_init(44100, -16, 2, 512)
        mixer.init()
        pygame.init()

        clock = pygame.time.Clock()
        fps = 60

        screen_width = 1000
        screen_height = 1000

        screen = pygame.display.set_mode((screen_width, screen_height))
       


        #define font
        font = pygame.font.SysFont('Bauhaus 93', 70)
        font_score = pygame.font.SysFont('Bauhaus 93', 30)


        #define game variables
        tile_size = 50
        game_over = 0
        main_menu = True
        level = 1
        max_levels = 7
        score = 0


        #define colours
        white = (255, 255, 255)
        blue = (0, 0, 255)

        bgimages=['citybg.png', 'citybg2.jpg', 'citybg3.jpg','citybg4.jpg']
        #load images
        img = random.choice(bgimages)
        bg = pygame.image.load(img)
        bg = pygame.transform.scale(bg,(screen_width,screen_height))
        restart_img = pygame.image.load('restart_btn.png')
        start_img = pygame.image.load('start_btn.png')
        exit_img = pygame.image.load('exit_btn.png')
        bg_img = bg

        #load sounds
        pygame.mixer.music.load('music.wav')
        pygame.mixer.music.play(-1, 0.0, 5000)
        coin_fx = pygame.mixer.Sound('coin.wav')
        coin_fx.set_volume(0.5)
        jump_fx = pygame.mixer.Sound('jump.wav')
        jump_fx.set_volume(0.5)
        game_over_fx = pygame.mixer.Sound('game_over.wav')
        game_over_fx.set_volume(0.5)


        def draw_text(text, font, text_col, x, y):
            img = font.render(text, True, text_col)
            screen.blit(img, (x, y))


        #function to reset level
        def reset_level(level):
            player.reset(100, screen_height - 230)
            blob_group.empty()
            platform_group.empty()
            coin_group.empty()
            lava_group.empty()
            exit_group.empty()

            #load in level data and create world
            if path.exists(f'level{level}_data'):
                pickle_in = open(f'level{level}_data', 'rb')
                world_data = pickle.load(pickle_in)
            world = World(world_data)
            #create dummy coin for showing the score
            score_coin = Coin(tile_size // 2, tile_size // 2)
            coin_group.add(score_coin)
            return world


        class Button():
            def __init__(self, x, y, image):
                self.image = image
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.clicked = False

            def draw(self):
                action = False

                #get mouse position
                pos = pygame.mouse.get_pos()

                #check mouseover and clicked conditions
                if self.rect.collidepoint(pos):
                    if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                        action = True
                        self.clicked = True

                if pygame.mouse.get_pressed()[0] == 0:
                    self.clicked = False


                #draw button
                screen.blit(self.image, self.rect)

                return action


        class Player():
            def __init__(self, x, y):
                self.reset(x, y)

            def update(self, game_over):
                dx = 0
                dy = 0
                walk_cooldown = 5
                col_thresh = 20

                if game_over == 0:
                    #get keypresses
                    key = pygame.key.get_pressed()
                    if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
                        jump_fx.play()
                        self.vel_y = -15
                        self.jumped = True
                    if key[pygame.K_SPACE] == False:
                        self.jumped = False
                    if key[pygame.K_LEFT]:
                        dx -= 5
                        self.counter += 1
                        self.direction = -1
                    if key[pygame.K_RIGHT]:
                        dx += 5
                        self.counter += 1
                        self.direction = 1
                    if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
                        self.counter = 0
                        self.index = 0
                        if self.direction == 1:
                            self.image = self.images_right[self.index]
                        if self.direction == -1:
                            self.image = self.images_left[self.index]


                    #handle animation
                    if self.counter > walk_cooldown:
                        self.counter = 0    
                        self.index += 1
                        if self.index >= len(self.images_right):
                            self.index = 0
                        if self.direction == 1:
                            self.image = self.images_right[self.index]
                        if self.direction == -1:
                            self.image = self.images_left[self.index]


                    #add gravity
                    self.vel_y += 1
                    if self.vel_y > 10:
                        self.vel_y = 10
                    dy += self.vel_y

                    #check for collision
                    self.in_air = True
                    for tile in world.tile_list:
                        #check for collision in x direction
                        if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                            dx = 0
                        #check for collision in y direction
                        if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                            #check if below the ground i.e. jumping
                            if self.vel_y < 0:
                                dy = tile[1].bottom - self.rect.top
                                self.vel_y = 0
                            #check if above the ground i.e. falling
                            elif self.vel_y >= 0:
                                dy = tile[1].top - self.rect.bottom
                                self.vel_y = 0
                                self.in_air = False


                    #check for collision with enemies
                    if pygame.sprite.spritecollide(self, blob_group, False):
                        game_over = -1
                        game_over_fx.play()

                    #check for collision with lava
                    if pygame.sprite.spritecollide(self, lava_group, False):
                        game_over = -1
                        game_over_fx.play()

                    #check for collision with exit
                    if pygame.sprite.spritecollide(self, exit_group, False):
                        game_over = 1


                    #check for collision with platforms
                    for platform in platform_group:
                        #collision in the x direction
                        if platform.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                            dx = 0
                        #collision in the y direction
                        if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                            #check if below platform
                            if abs((self.rect.top + dy) - platform.rect.bottom) < col_thresh:
                                self.vel_y = 0
                                dy = platform.rect.bottom - self.rect.top
                            #check if above platform
                            elif abs((self.rect.bottom + dy) - platform.rect.top) < col_thresh:
                                self.rect.bottom = platform.rect.top - 1
                                self.in_air = False
                                dy = 0
                            #move sideways with the platform
                            if platform.move_x != 0:
                                self.rect.x += platform.move_direction


                    #update player coordinates
                    self.rect.x += dx
                    self.rect.y += dy


                elif game_over == -1:
                    self.image = self.dead_image
                    draw_text('GAME OVER!', font, blue, (screen_width // 2) - 200, screen_height // 2)
                    if self.rect.y > 200:
                        self.rect.y -= 5

                #draw player onto screen
                screen.blit(self.image, self.rect)

                return game_over


            def reset(self, x, y):
                self.images_right = []
                self.images_left = []
                self.index = 0
                self.counter = 0
                for num in range(1, 5):
                    img_right = pygame.image.load(f'guy{num}.png')
                    img_right = pygame.transform.scale(img_right, (40, 80))
                    img_left = pygame.transform.flip(img_right, True, False)
                    self.images_right.append(img_right)
                    self.images_left.append(img_left)
                self.dead_image = pygame.image.load('ghost.png')
                self.image = self.images_right[self.index]
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.width = self.image.get_width()
                self.height = self.image.get_height()
                self.vel_y = 0
                self.jumped = False
                self.direction = 0
                self.in_air = True



        class World():
            def __init__(self, data):
                self.tile_list = []

                #load images
                dirt_img = pygame.image.load('platformground.png')
                grass_img = pygame.image.load('platformjump.jpg')

                row_count = 0
                for row in data:
                    col_count = 0
                    for tile in row:
                        if tile == 1:
                            img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                            img_rect = img.get_rect()
                            img_rect.x = col_count * tile_size
                            img_rect.y = row_count * tile_size
                            tile = (img, img_rect)
                            self.tile_list.append(tile)
                        if tile == 2:
                            img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                            img_rect = img.get_rect()
                            img_rect.x = col_count * tile_size
                            img_rect.y = row_count * tile_size
                            tile = (img, img_rect)
                            self.tile_list.append(tile)
                        if tile == 3:
                            blob = Enemy(col_count * tile_size, row_count * tile_size + 15)
                            blob_group.add(blob)
                        if tile == 4:
                            platform = Platform(col_count * tile_size, row_count * tile_size, 1, 0)
                            platform_group.add(platform)
                        if tile == 5:
                            platform = Platform(col_count * tile_size, row_count * tile_size, 0, 1)
                            platform_group.add(platform)
                        if tile == 6:
                            lava = Lava(col_count * tile_size, row_count * tile_size + (tile_size // 2))
                            lava_group.add(lava)
                        if tile == 7:
                            coin = Coin(col_count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2))
                            coin_group.add(coin)
                        if tile == 8:
                            exit = Exit(col_count * tile_size, row_count * tile_size - (tile_size // 2))
                            exit_group.add(exit)
                        col_count += 1
                    row_count += 1


            def draw(self):
                for tile in self.tile_list:
                    screen.blit(tile[0], tile[1])



        class Enemy(pygame.sprite.Sprite):
            def __init__(self, x, y):
                pygame.sprite.Sprite.__init__(self)
                self.image = pygame.image.load('blob.png')
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.move_direction = 1
                self.move_counter = 0

            def update(self):
                self.rect.x += self.move_direction
                self.move_counter += 1
                if abs(self.move_counter) > 50:
                    self.move_direction *= -1
                    self.move_counter *= -1


        class Platform(pygame.sprite.Sprite):
            def __init__(self, x, y, move_x, move_y):
                pygame.sprite.Sprite.__init__(self)
                img = pygame.image.load('platform.png')
                self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.move_counter = 0
                self.move_direction = 1
                self.move_x = move_x
                self.move_y = move_y


            def update(self):
                self.rect.x += self.move_direction * self.move_x
                self.rect.y += self.move_direction * self.move_y
                self.move_counter += 1
                if abs(self.move_counter) > 50:
                    self.move_direction *= -1
                    self.move_counter *= -1





        class Lava(pygame.sprite.Sprite):
            def __init__(self, x, y):
                pygame.sprite.Sprite.__init__(self)
                img = pygame.image.load('lava.png')
                self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y


        class Coin(pygame.sprite.Sprite):
            def __init__(self, x, y):
                pygame.sprite.Sprite.__init__(self)
                img = pygame.image.load('coin.png')
                self.image = pygame.transform.scale(img, (tile_size // 2, tile_size // 2))
                self.rect = self.image.get_rect()
                self.rect.center = (x, y)


        class Exit(pygame.sprite.Sprite):
            def __init__(self, x, y):
                pygame.sprite.Sprite.__init__(self)
                img = pygame.image.load('exit.png')
                self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 1.5)))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y



        player = Player(100, screen_height - 230) 
        print('player',screen_height-230)

        blob_group = pygame.sprite.Group()
        platform_group = pygame.sprite.Group()
        lava_group = pygame.sprite.Group()
        coin_group = pygame.sprite.Group()
        exit_group = pygame.sprite.Group()

        #create dummy coin for showing the score
        score_coin = Coin(tile_size // 2, tile_size // 2)
        coin_group.add(score_coin)

        #load in level data and create world
        if path.exists(f'level{level}_data'):
            pickle_in = open(f'level{level}_data', 'rb')
            world_data = pickle.load(pickle_in)
        world = World(world_data)


        #create buttons
        restart_button = Button(screen_width // 2 - 50, screen_height // 2 + 100, restart_img)
        start_button = Button(screen_width // 2 - 350, screen_height // 2, start_img)
        exit_button = Button(screen_width // 2 + 150, screen_height // 2, exit_img)


        run = True
        while run:

            clock.tick(fps)

            screen.blit(bg_img, (0, 0))

            if main_menu == True:
                if exit_button.draw():
                    run = False
                if start_button.draw():
                    main_menu = False
            else:
                world.draw()

                if game_over == 0:
                    blob_group.update()
                    platform_group.update()
                    #update score
                    #check if a coin has been collected
                    if pygame.sprite.spritecollide(player, coin_group, True):
                        score += 1
                        coin_fx.play()
                    draw_text('X ' + str(score), font_score, white, tile_size - 10, 10)
                
                blob_group.draw(screen)
                platform_group.draw(screen)
                lava_group.draw(screen)
                coin_group.draw(screen)
                exit_group.draw(screen)

                game_over = player.update(game_over)

                #if player has died
                if game_over == -1:
                    if restart_button.draw():
                        world_data = []
                        world = reset_level(level)
                        game_over = 0
                        score = 0

                #if player has completed the level
                if game_over == 1:
                    #reset game and go to next level
                    level += 1
                    if level <= max_levels:
                        #reset level
                        world_data = []
                        world = reset_level(level)
                        game_over = 0
                    else:
                        draw_text('YOU WIN!', font, blue, (screen_width // 2) - 140, screen_height // 2)
                        if restart_button.draw():
                            level = 1
                            #reset level
                            world_data = []
                            world = reset_level(level)
                            game_over = 0
                            score = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()

        pygame.quit()
