import random
import time
import pgzrun
import pygame
   
speed =2
player = Actor ("player")
enemy = Actor ("zombie")
coin = Actor ("coin")
score = 0
WIDTH = 1568
HEIGHT = 980
attack = False
enemys = []
meteor = 0
level_counter = 0
sounds.pixelspace.play(loops = -1)

def draw() :
    if enemy.colliderect(coin):
        screen.fill("red")
        
    else:
        screen.blit("pixelgrass",(0,0))
    player.draw()
    enemy.draw()
    coin.draw()
    screen.draw.text(f"Score: {score}", (10, 10))

    if meteor == 1 :
        meteor_actor = Actor ("meteor")
        meteor_actor.draw()
        


def update() :
    global score
    if keyboard.w :
        player.y -=10
    if keyboard.s :
        player.y +=10
    if keyboard.d :
        player.x +=10
    if keyboard.a :
        player.x -=10    
    if player.colliderect(coin):
        score += 1
        spawn_coin()
    zombie() 
    
    
def spawn_coin() :
    coin.x = random.randint(10,1567)
    coin.y = random.randint(10,979)
        
def zombie() :
    global speed
    animate(enemy, pos=coin.pos, duration=speed)

spawn_coin()

def speedincrease() :
    global speed
    speed -= 0.1
def level() :
    global level_counter, meteor
    level_counter += 1   
    if level_counter == 1 :
        meteor = 1
def fall() :
    pass





clock.schedule_interval(speedincrease,5) 
clock.schedule_interval(level,10)
clock.schedule_interval(fall,10)      
pgzrun.go()