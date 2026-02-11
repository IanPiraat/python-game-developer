import pgzrun
import pygame
import random
score = 0
game = True
WIDTH = 870
HEIGHT = 648

cars = ["orangecar","greencar","redcar"]
player = Actor("blackcar")
enemy = Actor("orangecar")



player.x = WIDTH / 2
player.y = 500
enemy.x = random.randint(200,600)
enemy.y = 0



def draw() :
    screen.fill("green")
    screen.blit("road",(0,0))
    player.draw()
    enemy.draw()
    enemy.y += 5
    if game == False :
        screen.fill("red")
        screen.draw.text(f"final score = {score}",(50,50),fontname = "arial", fontsize=100,color = "white")
        


def enemy1 () :  
    global game 
    global cars
    global score
    if game == True :

        enemy.y += 5
        if enemy.y >= 620 :
            score += 1
            enemy.image = (random.choice(cars))
            enemy.y = 0
            enemy.x = random.randint(200,600)

    
def update() :
    global game
    if keyboard.a and player.x >= 200 :
        player.x -= 10
    if keyboard.d and player.x <= 650 :
        player.x += 10 
    

    if player.colliderect(enemy):
        game = False     
    enemy1()   
     
    
pgzrun.go()




    