import pgzrun
import pygame
import random
WIDTH = 800
HEIGHT = 422
timefall = 3
items = ["battery", "plasticbag","bottle","chips",]
currentlevel = 1
finalround = 10
gameover = False
gamecomplete = False
players = []
animations = []
sounds.bg.play(loops = -1)
def draw():
    screen.blit("forest",(0, 0))
    if gameover == True:
        screen.fill("red")
        screen.draw.text("Game Over", center=(WIDTH/2, HEIGHT/2), fontsize=60, color="white")
    elif gamecomplete == True:
        sounds.bg.stop()
        sounds.win.play()
        screen.fill("green")
        screen.draw.text("You Win!", center=(WIDTH/2, HEIGHT/2), fontsize=60, color="white")
        while True :
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

def on_mouse_down(pos) :
    global players,currentlevel
    for player in players :
        if player.collidepoint(pos) :
            if player.image == "paperbag" :
                sounds.collectpaper.play()
                handlegamecomplete()
            else :
                gameover = True
                handlegameover()
                    

    

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
       
        animation = animate(player,y=HEIGHT,duration = timefall,on_finished = handlegameover)
        animations.append(animation)
def handlegamecomplete() :
    global currentlevel,finalround,gameover,gamecomplete,animations,players,timefall
    for animation in animations :
        if animation.running:
            animation.stop()
    if currentlevel < finalround :
        currentlevel += 1
        timefall -= 0.15

        players = []
        animations = []
    else :
        gamecomplete = True    
def shuffle() :
    global players
    if players:
        random.shuffle(players)
        layoutsitems()
clock.schedule_interval(shuffle,1.2)

        











pgzrun.go()    