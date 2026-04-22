import random
import time
import pgzrun
import pygame
gameover = False
speed = 2
player = Actor("player")
enemy = Actor("zombie")
coin = Actor("coin")
meteor_actor = Actor("meteor")
score = 0
WIDTH = 1568
HEIGHT = 980
attack = False
enemys = []
meteor = 0
level_counter = 0
sounds.pixelspace.play(loops=-1)

player.x = WIDTH / 2
player.y = HEIGHT / 2
enemy.x = 100
enemy.y = 100
coin.x = random.randint(10, 1567)
coin.y = random.randint(10, 979)
meteor_actor.x = 0
meteor_actor.y = 0

def draw():
    global gameover0
    if gameover:
        screen.fill("red")
        screen.blit("gameover", (0, 0))
    else:
        screen.blit("pixelgrass", (0, 0))
        player.draw()
        enemy.draw()
        coin.draw()
        screen.draw.text(f"Score: {score}", (10, 10),fontsize=30, color="white")
        if meteor == 1:
            meteor_actor.draw()

def update():
    global score, meteor_actor, meteor, gameover

    if keyboard.w:
        player.y -= 10
    if keyboard.s:
        player.y += 10
    if keyboard.d:
        player.x += 10
    if keyboard.a:
        player.x -= 10
    if player.colliderect(coin):
        score += 1
        spawn_coin()
    if player.colliderect(meteor_actor):
        gameover = True
    zombie()

    if meteor == 1:
        meteor_actor.x -= 10
        meteor_actor.y += 10

        if meteor_actor.x == 200:
            meteor = 0

def spawn_coin():
    coin.x = random.randint(10, 1567)
    coin.y = random.randint(10, 979)

def zombie():
    global speed
    animate(enemy, pos=coin.pos, duration=speed)

def speedincrease():
    global speed
    speed -= 0.1

def level():
    global level_counter, meteor
    meteor_actor.y = 0
    meteor_actor.x = random.randint(0, 1567)
    meteor = 1

def fall():
    pass

clock.schedule_interval(speedincrease, 5)
clock.schedule_interval(level, 3)
clock.schedule_interval(fall, 10)
pgzrun.go()