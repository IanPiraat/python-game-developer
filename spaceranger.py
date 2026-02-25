import pgzrun
import random
import pygame
import time

game = 0
WIDTH = 1250
HEIGHT = 720
player = Actor ("pixeljet")

player.x = 600
player.y = 720 
bullets = []
enemys = []
score = 0



for x in range (5) :
    for y in range(5) :
        enemy = Actor ("pixelfly")
        enemy.y = 50 + y * 100
        enemy.x = 400 + x * 100   
        enemys.append(enemy) 
        

def draw():
    screen.blit("spacebackground",(0,0))
    for enemy in enemys :
        enemy.draw()
    player.draw()
    for bullet in bullets :
        bullet.draw()
    if game == 1 :
        screen.fill("red")
        screen.draw.text(f"score:{score}",(200,225),fontname = "arial", fontsize=100,color = "white")


def on_key_down (key) :
    if key == keys.SPACE :
        bullet = Actor("bullet")
        bullets.append(bullet)
        bullet.x = player.x
        bullet.y = player.y




def update():
    global score
    global bullets
    global game
    if keyboard.a and player.x > 0 :
        player.x -= 5 
    if keyboard.d and player.x < 1250 :
        player.x += 5 
    if keyboard.w and player.y > 0 :
        player.y -= 5 
    if keyboard.s and player.y < 720 :
        player.y += 5        
    for bullet in bullets :
        bullet.y -= 10
        if bullet.y < 0 :
            bullets.remove(bullet)
            
    for enemy in enemys :
        enemy.y += 0.25
        for bullet in bullets :
            if enemy.colliderect(bullet) :
                score += 1
                enemys.remove(enemy)
                bullets.remove(bullet)
        if enemy.colliderect(player) :
            game = 1
        if enemy.y >= 720 :
           game = 1     

        


pgzrun.go()