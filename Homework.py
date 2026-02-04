import pgzrun
import pygame
import random
k = 1

WIDTH = 1500
HEIGHT = 2000


vector = Actor("neutral")
vector2 = Actor("happy")
vector.x = WIDTH / 2
vector.y = HEIGHT / 2
vector2.x = WIDTH / 2
vector2.y = HEIGHT / 2
    


show_happy = False

def draw():
    screen.fill("black")
    vector.draw()

def on_mouse_down(pos):
    global show_happy
    if vector.collidepoint(pos):
        if show_happy == False :
            show_happy = True
            vector.image = "happy"
            vector.x = random.randint(50,1450)
            vector.y = random.randint(100,1900)

        else :
            show_happy = False
            vector.image = "neutral"



pgzrun.go()