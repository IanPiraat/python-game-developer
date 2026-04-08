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
timeleft = 15
game = True
question = []
questions = []
score = 0
answerboxes=[answerbox1,answerbox2,answerbox3,answerbox4]

sounds.quiz.play(loops = -1)
def draw() : 
    screen.fill("black")
    screen.draw.filled_rect(titlebox,"black")
    screen.draw.textbox("Hello and welcome to the quiz :)",titlebox,color = "white")
    screen.draw.filled_rect(questionbox,"blue")
    screen.draw.textbox(question[0].strip(),questionbox,color="black")
    screen.draw.filled_rect(timerbox,"red")
    screen.draw.textbox("{}".format(timeleft),timerbox,color = "black" )
    screen.draw.filled_rect(answerbox1,"green")
    screen.draw.textbox(question[1].strip(),answerbox1,color="black")
    screen.draw.filled_rect(answerbox2,"orange")
    screen.draw.textbox(question[2].strip(),answerbox2,color="black")
    screen.draw.filled_rect(skipbox,"purple")
    screen.draw.textbox("Skip",skipbox,color = "black")
    screen.draw.filled_rect(answerbox3,"magenta")
    screen.draw.textbox(question[3].strip(),answerbox3,color="black")

    screen.draw.filled_rect(answerbox4,"yellow")
    screen.draw.textbox(question[4].strip(),answerbox4,color="black")
    screen.draw.filled_rect(resetbox,"pink")
    screen.draw.textbox("Reset",resetbox,color = "black")

def update_time () :
    global game
    global timeleft
    if timeleft > 0 :
        timeleft -= 1
    else :
        game = False
        
def game_over () :
    global question,timeleft
    global score
    global game
    message = 'game over score is {}'.format(score)
    question = [message,'-','-','-','-',5]
    timeleft = 0
    game = False
    
def read() :
    global questions
    global question
    file = open("quiz.txt","r")
    for item in file :
        questions.append(item.strip())

read()
print(questions)

def readnextquest() :
    global questions
    global question
    question = questions.pop(0).split('|')
    
readnextquest()

def update() :
    global skipbox,timeleft,question
    titlebox.x -= 2
    if titlebox.right < 0 : 
        titlebox.left = 750
    if game == False :
        game_over()

def on_mouse_down(pos) :
    sounds.click.play()
    global answerboxes,question,score,timeleft,game,questions
    index =1

    if skipbox.collidepoint(pos) :
        readnextquest()
        timeleft = 15
    if resetbox.collidepoint(pos) :
        questions = []  
        read()
        game = True
        readnextquest()
        timeleft = 15
        score = 0    

    for box in answerboxes:
        if box.collidepoint(pos):
            if index == int(question[5]) :
                sounds.correct.play()
                readnextquest()
                score += 1
                timeleft = 15
            else :
                sounds.wrong.play()
                game_over()  
        index +=1
           
                







clock.schedule_interval(update_time,1)
pgzrun.go()
