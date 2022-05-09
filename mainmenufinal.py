#Stephanie Rojas
# learning how to draw circles and rectangles
#use keys to move objects
#Using Dictionaries

#Objective of the game is for the rect to run away fom the circle, if they collide the circle etas the square, 
#circle will  get larger, and a new rect should appear somewhere on the screen
# K_UP                  up circle
# K_DOWN                down circle
# K_RIGHT               right circle
# K_LEFT                left circle
# K_a                   left square
# K_d                   right square
# K_w                   up square
# K_s                   down square
# K_SPACE               jump
#initialize pygame

import os, random, time, pygame, math, datetime
from turtle import screensize
from pygame.locals import *
os.system('cls')
name=input("What is your name? ")
#initialize pygame
pygame.init()

#Declare constants, variables, list, dictionaries, any object
#scree size
WIDTH=700
HEIGHT=700
xMs=50
yMs=250
wb=30
hb=30
MAIN=True
INST=False
SETT=False
LEV_I=False
LEV_II=False
LEV_III=False
SCORE=False
#List f messages
MenuList=['Instructions','Settings', "Level I","Level II",'Level III','Scoreboard','Exit']
SettingList=['Screen Size','Backgrnd Color','Icon','']
sizeList=['1000 x 1000','800 x 800','600 x 600']
check=True #for the while loop

#create screen
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Platformer')

#define colors
colors={'white':[255,255,255], 'red':[255,0,0], 'aqua':[102,153, 255],
'orange':[255,85,0],'purple':[48,25,52],'navy':[5,31,64],'pink':[200,3,75]}
#Get colors
background= colors.get('white')
randColor=''
cr_color=colors.get('aqua')
sqM_color=colors.get('pink')
BLACK=(0,0,0)
#create fifferent type 
TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('comicsans', 40)
INST_FNT=pygame.font.SysFont('comicsans', 30)
#Create square fr menu

squareM=pygame.Rect(xMs,yMs,wb,hb)
#Create Title
def TitleMenu(Message):
    text=TITLE_FNT.render(Message, 1, (255,0,0))
    screen.fill((255,255,255))
    #get the width  the text 
    #x value = WIDTH/2 - wText/2
    xt=WIDTH/2-text.get_width()/2
    screen.blit(text,(xt,50))
#This is a function uses a parameter
def MainMenu(Mlist):
    txty=243
    squareM.y=250
    for i in range(len(Mlist)):
        message=Mlist[i]
        text=INST_FNT.render(message,1,(51,131,51))
        screen.blit(text,(90,txty))
        pygame.draw.rect(screen,sqM_color, squareM )
        squareM.y +=50
        txty+=50
    pygame.display.update()
    pygame.time.delay(10)
def changeColor():
    global randColor
    colorCheck=True
    while colorCheck:
        randColor=random.choice(list(colors))
        if colors.get(randColor)==background:
            print(randColor)
            print(background)
            randColor=random.choice(list(colors))
        else:
            colorCheck=False
def instr():
    print("in instr")
    myFile=open('instructions.txt')
    yi=150
    stuff= myFile.readlines()


    print(stuff)
    for line in stuff:
        print(line)
        text=INST_FNT.render(line, 1, BLACK)
        screen.blit(text, (40,yi))
        pygame.display.update()
        pygame.time.delay(50)
        yi+=50
    myFile.close()
def keepScore(score):
    date=datetime.datetime.now()
    print(date.strftime('%m/%d/%Y'))
    scoreLine=str(score)+"\t"+name+"\t"+date.strftime('%m/%d/%Y'+'\n')
 
    #open a file and write in it 
    # when y write it erases the prev 
    myFile=open('score.txt','a') 
    myFile.write(scoreLine)
    myFile.close()
def scoreBoard():
    myFile=open('score.txt', 'r')
    yi=150
    stuff= myFile.readlines()
    myFile.close()
    stuff.sort()
    N=len(stuff)-1
    temp=[]
    j=0
    for i in range(N, -1, -1):
        print(i,stuff[i])
        # temp[j]=stuff[i]
        #     j +=1
        # print(temp)
        # for i in range(N):
        #     text=INST_FNT.render(temp[i], 1, BLACK)
        #     screen.blit(text, (40,yi))
        #     pygame.display.update()
        #     pygame.time.delay(50)
        #     yi+=50
    
def keepScore(score):
    date=datetime.datetime.now()
    print(date.strftime('%m/%d/%Y'))
    scoreLine='\n'+str(score)+"\t"+name+"\t"+date.strftime('%m/%d/%Y'+'\n')
 
    #open a file and write in it 
    # when y write it erases the prev 
    myFile=open('score.txt','a') 
    myFile.write(scoreLine)
    myFile.close()
def changeScreenSize(xm,ym):
    global HEIGHT, WIDTH, screen
    if ((xm >20 and xm <80) and (ym >250 and ym <290)):
        HEIGHT=1000
        WIDTH=1000

    if ((xm >20 and xm <80) and (ym >300 and ym <330)):
        HEIGHT=800
        WIDTH=800
        
    if ((xm >20 and xm <80) and (ym >350 and ym <380)):
        HEIGHT=600
        WIDTH=600
    screen=pygame.display.set_mode((WIDTH,HEIGHT))
 


    
    def playGame():
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

        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption('Platformer')


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
        bg = random.choice(bgimages)
        restart_img = pygame.image.load('restart_btn.png')
        start_img = pygame.image.load('start_btn.png')
        exit_img = pygame.image.load('exit_btn.png')
        bg_img = pygame.image.load(bg)

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
        player.reset(100, screen_height - 130)
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



    player = Player(100, screen_height - 130)

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

         
    #sq_color=colors.get('navy')
    #Making a rand c f the square
    

    #==============================================
    #
    #Beginning  main program``
    sq_color=colors.get(randColor)
    keys=pygame.key.get_pressed()
    mouse_pos=(0,0)
    screCk=True
    first=True
    xm=0 
    ym=0
    f_SEET=True
    sc_size=False
    set_first=True
    c_first=True
    while check:
        for case in pygame.event.get():
            if case.type==pygame.QUIT:
                check=False
            if case.type ==pygame.MOUSEBUTTONDOWN:
                mouse_pos=pygame.mouse.get_pos()
                xm= mouse_pos[0]
                ym= mouse_pos[1]
            # print(mouse_pos)
        keys=pygame.key.get_pressed() #this returns a list
        if MAIN:
            screen.fill(background)
            TitleMenu("MENU")
            MainMenu(MenuList)
        if INST and first:
            screen.fill(background)
            TitleMenu("INSTRUCTIONS")
            instr()
            first=False
        if INST:
            if keys[pygame.K_ESCAPE]:
                INST=False
                MAIN=True
                first=True
        if SETT and f_SEET:
            screen.fill(background)
            TitleMenu("SETTINGS")
            MainMenu(SettingList)
            f_SEET=False
        if SETT:
            if keys[pygame.K_ESCAPE]:
                SETT=False
                MAIN=True
                f_SEET=True
        if LEV_I:
            screen.fill(background)
            playGame()
            LEV_I=False
            MAIN=True
            xm=0
            ym=0
        if LEV_II:
            screen.fill(background)
            TitleMenu("LEVEL II")
            if keys[pygame.K_ESCAPE]:
                LEV_II=False
                MAIN=True
        if LEV_III:
            screen.fill(background)
            TitleMenu("LEVEL III")
            if keys[pygame.K_ESCAPE]:
                LEV_III=False
                MAIN=True
        if SCORE and screCk:
            screen.fill(background)
            TitleMenu("SCOREBOARD")
            scoreBoard()
            #call funct t print scres
            screCk=False
        if SCORE:
            if keys[pygame.K_ESCAPE]:
                SCORE=False
                MAIN=True
                screCk=True
        if ((xm >20 and xm <80) and (ym >250 and ym <290)) and MAIN:
            MAIN=False
            INST=True
        if ((xm >20 and xm <80) and (ym >300 and ym <330))and MAIN:
            MAIN=False
            SETT=True  
        if ((xm >20 and xm <80) and (ym >350 and ym <380))and MAIN :
            MAIN=False
            LEV_I=True   
        if ((xm >20 and xm <80) and (ym >400 and ym <430))and MAIN :
            MAIN=False
            LEV_II=True   
        if ((xm >20 and xm <80) and (ym >450 and ym <480))and MAIN:
            MAIN=False
            LEV_III=True   
        if ((xm >20 and xm <80) and (ym >500 and ym <530))and MAIN:
            MAIN=False
            SCORE=True 
        if ((xm >20 and xm <80) and (ym >250 and ym <290)) and SETT and set_first:  
            screen.fill(background)
            TitleMenu("Screen Size")
            MainMenu(sizeList )
            sc_size=True
            set_first=False
            f_SEET=True
            if keys[pygame.K_ESCAPE]:
                sc_size=False
                set_first=True
        if sc_size and xm >0:
            changeScreenSize(xm,ym)
            screen.fill(background)
            TitleMenu("Screen Size")
            MainMenu(sizeList )
            if keys[pygame.K_ESCAPE]:
                sc_size=False
                set_first=True
        if ((xm >20 and xm <80) and (ym >300 and ym <330))and SETT and c_first:
            screen.fill(background)
            TitleMenu("Background Color")
            c_first=False
            if keys[pygame.K_ESCAPE]:
                c_first=True
                set_first=True
        if ((xm >20 and xm <80) and (ym >550 and ym <580)) :
            screen.fill(background)
            keepScore(121)
            text=INST_FNT.render("Make sure you update the score file", 1, BLACK)
            screen.blit(text, (40,200))
            text=INST_FNT.render("before you exit", 1, BLACK)
            screen.blit(text, (40,300))
            text=INST_FNT.render("Thank you for playing", 1, BLACK)
            screen.blit(text, (40,400))
            pygame.display.update()
            pygame.time.delay(50)
            MAIN=False
            SCORE=False 
            pygame.time.delay(3000)
            check=False
        pygame.display.update()
        pygame.time.delay(10)

    os.system('cls')
    pygame.quit()