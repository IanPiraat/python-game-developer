import random 
import time
import pgzrun
import pygame


WIDTH = 512
HEIGHT = 544


player = Actor ("ship")


player.x = WIDTH / 2
player.y = HEIGHT / 2
color = ["greenenemy","greyenemy","redenemy","blueenemy"]
enemys = []
health = 1
lives = 5
attack = False
speed = 6
enemyspeed = 2
game = True
killstreak = 0
shake = 0
shake_strength = 5

sounds.shiptarget.play(loops = -1)
def draw() :
    global shake
    global game

    if game == True :
        offset_x = random.uniform(-shake, shake)
        offset_y = random.uniform(-shake, shake)
        global shake_strength
        screen.blit("map",(offset_x,offset_y))
        player.draw()
        for enemy in enemys:
            enemy.x += offset_x
            enemy.y += offset_y
            enemy.draw()
            enemy.x -= offset_x
            enemy.y -= offset_y
            if shake >= 0 :
                shake -= 0.7
          

    
        screen.draw.text("lives = {}".format(lives) ,(50,50))
        for enemy in enemys :
            
            enemy.draw()
            if enemy.image == "greenenemy":
                enemyspeed = random.uniform(0.5,1.5)
            elif enemy.image == "greyenemy":
                enemyspeed = 0.75
            elif enemy.image == "redenemy":
                enemyspeed = 0.5
            elif enemy.image == "blueenemy":
                enemyspeed = 0.1
                

            
            animate(enemy,pos=player.pos,duration = enemyspeed)
    else : 
       screen.fill("red")
       screen.draw.text("game over",(65,250),fontsize=100) 


def update() :
    global shake
    global lives
    global speed
    global health
    global lives
    global game
    global killstreak
    for enemy in enemys :
        if attack == False : 
            if enemy.colliderect(player) :
                if enemy.image == "blueenemy" :
                    lives -= 2  
                    speed = 7
                elif enemy.image == "greyenemy":
                    speed = 6    
                else :
                    lives -= 1
                shake = 2
                sounds.oef.play() 
                enemys.remove(enemy)
        else:
            if enemy.colliderect(player) :
                
                if enemy.image == "greenenemy":
                    health += 1
                    killstreak += 1
                    sounds.blip.play()
                elif enemy.image == "greyenemy":
                    speed -= 0.5
                    sounds.upgrade.play()
                    killstreak += 1
                    sounds.blip.play()

                elif enemy.image == "redenemy":
                    lives += 1
                    killstreak += 1
                    sounds.blip.play()
                elif enemy.image == "blueenemy":
                    speed -= 1
                    sounds.upgrade.play()
                    killstreak += 1
                    sounds.blip.play()  
                    if killstreak >= 2:
                        sounds.betakill.play()

                enemys.remove(enemy)   

                
    if lives < 1 :
        game = False
        

        
    if speed < 0.1 :
         speed = 0.2            

    
             
def attackmode() :
    global attack
    attack = False
    

        
               

def on_mouse_down (pos) :
    global attack
    global speed
    if attack == False :
        attack = True
        
    animate(player,pos = pos,duration = speed,angle = player.angle_to(pos)-90,on_finished=attackmode)
    

def spawnenemy () :
    img = random.choice(color)
    enemy = Actor (img)
    enemys.append(enemy)
    if img == "greenenemy" :
        enemy.x = 0
        enemy.y = 0

    if img == "greyenemy" :
        enemy.x = 512
        enemy.y  =544
    if img == "redenemy" :
        enemy.x=0
        enemy.y=544
    if img == "blueenemy" :
        enemy.x = 512
        enemy.y = 0        




if game == True :
    clock.schedule_interval(spawnenemy,2)
else :
    enemys = []
        
pgzrun.go()    