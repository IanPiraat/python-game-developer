import pgzrun
import pygame
import random
WIDTH = 800
HEIGHT = 422

items = ["battery", "plasticbag","bottle","chips",]
currentlevel = 1
finalround = 10
gameover = False
gamecomplete = False
players = []
animations = []

def draw():
    screen.blit("forest",(0, 0))
    if gameover == True:
        screen.fill("red")
        screen.draw.text("Game Over", center=(WIDTH/2, HEIGHT/2), fontsize=60, color="white")
    elif gamecomplete == True:
        screen.fill("green")
        screen.draw.text("You Win!", center=(WIDTH/2, HEIGHT/2), fontsize=60, color="white")    
    else :
        for player in players:
            player.draw()

def update():
    if len (players) == 0:
        makeplayer()
        layoutsitems()
        animateitems()

def makeplayer():
    global players,currentlevel
    player = Actor ("paperbag")
    players.append(player)
    for i in range (currentlevel) :
        item = Actor (random.choice(items))
        players.append(item)
def layoutsitems() :
    global players
    gaps = len(players) + +1
    gapsize = WIDTH / gaps
    random.shuffle(players)
    index = 1   
    for player in players :
        player.x = gapsize * index
        index += 1
def handlegameover() :
    global gameover 
    gameover = True
def animateitems() :
    global animations,players
    for player in players :
        animate(player,y=HEIGHT,duration = 3,on_finished = handlegameover)
        animation = animate(player,y=HEIGHT,duration = 3,on_finished = handlegameover)
        animations.append(animation)












pgzrun.go()    