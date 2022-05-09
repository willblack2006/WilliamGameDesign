#learn pygame
#import libs
import os, time
import pygame as pg
WIDTH = 600
HEIGHT = 700
#initialize pygame
pg.init()
#create window/screen
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('My Screen')
pg.display.update()
pg.time.delay(500)
#create new colors
colors={'red':[255,0,0],'white':[255, 255, 255],'blueish' :[102, 153, 255]}
background=
white = [255, 255, 255]
blueish = [102, 153, 255]
green = [0, 255, 0]
red = [235, 64, 52]
orange = [230, 127, 9]
hotpink = [230, 9, 215]
blue = [9, 13, 230]
cyan = [9, 193, 230]
lime = [9, 219, 51]
yellow = [240, 229, 81]
screen.fill(white)
pg.display.update()
pg.time.delay(500)
#make rectangles
    #initial pos
x = 10
y = 10
#height and width of rect
wbox = 20
hbox = 20
square = pg.Rect(x, y, wbox, hbox)


#game loop
run = True
while run:
    screen.fill(blueish)
    pg.draw.rect(screen, (green), square)
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    pg.time.delay(200)
    #cahnge value of certain var
    square.x += 5
    square.y += 5
    pg.draw.rect(screen, (green), square)
    pg.display.update()
    pg.time.delay(200)