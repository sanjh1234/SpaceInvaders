import pygame as py
import random as rd
import math
import time


#initialising pygame
py.init()

sc = py.display.set_mode((800,600))

#anything happening inside game windowis an event (any kind of game control)

#changing title and icon
py.display.set_caption("SPACE FIGHTER")

icon = py.image.load("001-rocket.png")
py.display.set_icon(icon)


#changing bg image
bg=py.image.load("space-bg.png")


#score
score = 0 
font = py.font.Font("freesansbold.ttf",24)
textx = 630
texty = 10


#game over text
g_o = py.font.Font("freesansbold.ttf",64)
gox = 200
goy = 240


#player
playerimg=py.image.load("001-space.png")
pl_x =370
pl_y =490
pl_chg=0


#enemy
enmimg=[]
enm_x =[]
enm_y =[]
enm_xchg=[]
enm_ychg=[]

no_of_enm=6

for i in range(no_of_enm):
    enmimg.append(py.image.load("002-space-ship.png"))
    enm_x .append(rd.randint(0,800))
    enm_y .append(rd.randint(0,300))
    enm_xchg.append(2)
    enm_ychg.append(30)


#bullet
bltimg=py.image.load("001-bullet.png")
blt_x =0
blt_y =490
blt_xchg=0
blt_ychg=20

# there are two states of bullet ready and fire
# ready - cant't see bullet at screem
# fire - bullet is currently moving
blt_state = "ready"


#explosion
expimg=py.image.load("001-supernova.png")
exp_x = 0
exp_y = 0


#finishing line
lineimg=py.image.load("001-minus.png")
linex = 0
liney = 420



def show_score(x,y):
    scr = font.render("Score : "+ str(score),True, (192,192,192))
    sc.blit(scr,(x,y))


def go_text(x,y):
    gotext = g_o.render("GAME OVER",True, (192,192,192))
    sc.blit(gotext,(x,y))


def enm(x,y,i):
    sc.blit(enmimg[i], (x,y))


def player(x,y):
    #x and y are introduced to move the player 
    sc.blit(playerimg, (x,y))


def fire_blt(x,y):
    #global is used to call the variable outside the function we can use the variable defined inside the "def" anywhere outside def
    global blt_state
    blt_state = "fire" 
    sc.blit(bltimg, (x+19,y+10))


def explosion(x,y):
    sc.blit(expimg,(x,y))


def finish_line(x,y):
    sc.blit(lineimg,(x,y))


#for bullet enemy collision
def collision(enmx,enmy,bltx,blty):
    dist = math.sqrt((pow(enmx-bltx,2))+(pow(enmy-blty,2)))
    if dist < 25:
        return True



#we are ganna draw all our elements in this loop
#game loop
running=True
while running:
    py.display.update()


    #adding bg color and img
    sc.fill(("black"))
    sc.blit(bg,(0,0))


    #this module make sure that all the events happens inside the loop
    for event in py.event.get():
        if event.type == py.QUIT:
            running=False
        
        #if keystroke is pressed check whether its right or left(keyboard binding)
        if event.type == py.KEYDOWN:
            if event.key == py.K_LEFT:
                pl_chg -= 4.5
            if event.key == py.K_RIGHT:
                pl_chg += 4.5

            if event.key == py.K_SPACE:
                if blt_state is "ready":
                    blt_x = pl_x
                    fire_blt(blt_x,blt_y)

        if event.type == py.KEYUP:
            if event.key == py.K_LEFT or event.key == py.K_RIGHT:
                pl_chg=0


    #this is to update our window and change x regulaly when right or left is pressed
    pl_x += pl_chg      

    #border checking for player
    if pl_x < -5:
        pl_x = -5
    if pl_x > 740:
        pl_x =740


    #for is included to manage every single enemy
    for i in range(no_of_enm):

        #game over
        if enm_y[i] > 400:
            for j in range(no_of_enm):
                time.sleep(0.2)
                enm_y[j] = 2000
            go_text(gox,goy)
            break

        #enemy movement
        enm_x[i] += enm_xchg[i]

        #border checking for enemy 
        if enm_x[i] < -10:
            enm_x[i] = -10
            enm_y[i] += enm_ychg[i] 
            enm_xchg[i] *= -1
        if enm_x[i] > 745:
            enm_x[i] =745
            enm_y[i] += enm_ychg[i] 
            enm_xchg[i] *= -1

        #bullet enemy collision
        col = collision(enm_x[i],enm_y[i],blt_x,blt_y)
        if col:
            blt_y = 490
            blt_state = "ready"

            exp_x =enm_x[i]
            exp_y =enm_y[i]
            explosion(exp_x,exp_y)

            enm_x[i] =rd.randint(0,800)
            enm_y[i] =rd.randint(0,350)
            score += 10
            print(score)

        enm(enm_x[i],enm_y[i],i)


    #bullet movement
    if blt_y < 0 :
        blt_y = 490
        blt_state = "ready"

    if blt_state is "fire":
        blt_y -= blt_ychg
        fire_blt(blt_x,blt_y)

    
    player(pl_x,pl_y)
    show_score(textx,texty)
    finish_line(linex,liney)
    
    