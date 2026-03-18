import pgzrun
import pygame
import random
import time

WIDTH = 620
HEIGHT = 352

robot = Actor ("robot")
dot = Actor("dot")

def draw() :
    robot.draw()
    dot.draw()


def update() :
    screen.blit("metal",(0,0))


def place() :
    dot.x = random.randint(50,600)
    dot.y = random.randint(50,320)

    animate(robot,pos=dot.pos,duration=0.5,on_finished=wait_then_move)



def wait_then_move() :
    sounds.beep.play()
    clock.schedule(place, 1)

   
place()

pgzrun.go()   