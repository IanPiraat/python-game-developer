import pgzrun
import pygame
import time
import random


HEIGHT = 560
WIDTH = 750

titlebox = Rect(0,0,750,75)
questionbox = Rect(10,85,550,150)
timerbox = Rect(570,85,170,150)
answerbox1 = Rect(10,245,270,150)
answerbox2 = Rect(290,245,270,150)
skipbox = Rect(570,245,170,150)
answerbox3 = Rect(10,405,270,150)
answerbox4 = Rect(290,405,270,150)
resetbox = Rect(570,405,170,150)
def draw() : 
    screen.fill("black")
    screen.draw.filled_rect(titlebox,"black")
    screen.draw.textbox("Hello and welcome to the quiz :)",titlebox,color = "white")
    screen.draw.filled_rect(questionbox,"blue")
    screen.draw.filled_rect(timerbox,"red")
    screen.draw.filled_rect(answerbox1,"green")
    screen.draw.filled_rect(answerbox2,"orange")
    screen.draw.filled_rect(skipbox,"purple")
    screen.draw.textbox("Skip",skipbox,color = "black")
    screen.draw.filled_rect(answerbox3,"magenta")
    screen.draw.filled_rect(answerbox4,"yellow")
    screen.draw.filled_rect(resetbox,"pink")
    screen.draw.textbox("Reset",resetbox,color = "black")


def update() :
    titlebox.x -= 2
    if titlebox.right < 0 : 
        titlebox.left = 750






pgzrun.go()    