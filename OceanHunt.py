import pygame
import pgzrun
import random
import time
Game = True
score = 0
HEIGHT = 454
check = 1
WIDTH = 740
pearls = []
diver = Actor("diver")
pearl = Actor("pearl")
crab = Actor("crab")
num = 1
diver.y = 225
diver.x = 370
sounds.underwatermusic.play(loops = -1)
crab.y = 420
crab.x = 370



def draw() :
    global score
    global Game
    screen.blit("backgroundwater",(0,0))
    if Game == True :
        Actor.draw(diver)
        for pearl in pearls:
            pearl.draw()
        Actor.draw(crab)
    screen.draw.text(f"score:{score}",(10,10),fontname = "arial", fontsize=32,color = "white")
    if Game == False :
        sounds.gameover.play()
        Game = "end"
    elif Game == "end" :
        screen.fill("red")
        screen.draw.text(f"score:{score}",(370,225),fontname = "arial", fontsize=100,color = "white")

def update():
    userInput()
    crab_npc()
    global pearls
    global Game
    global score
    global check
    global num
    for pearl in pearls :
        if diver.colliderect(pearl):
            sounds.collect.play()
            pearl.x = random.randint(50,700)
            pearl.y = random.randint(50,400)  
            score += 1
    if diver.colliderect(crab):
        diver.x = 0
        diver.y = 0
        
        Game = False
    if check == 1 or check == 2 :
        if len (pearls)==0 or len(pearls) <= 4 :
        
            for i in range (num) :
                pearl = Actor("pearl")
                pearl.x =random.randint(50,700)
                pearl.y =random.randint(50,400)
                pearls.append(pearl)
    if score > 5 :  
        check = 2
        num = 5
            

def crab_npc():
    move_speed = 3

    if keyboard.a and diver.x > 0 :
        crab.x -= move_speed
    if keyboard.d and diver.x < 740 :
        crab.x += move_speed

def userInput():    
    move_speed = 5

    if keyboard.a and diver.x > 0 :
        diver.image = "diver2"
        diver.x -= move_speed 
    if keyboard.d and diver.x < 740 :
        diver.image = "diver"
        diver.x += move_speed 
    if keyboard.w and diver.y > 0 : 
        diver.y -= move_speed
    if keyboard.s and diver.y < 454 : 
        diver.y += move_speed           










pgzrun.go()









