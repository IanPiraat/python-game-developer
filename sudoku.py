import pgzrun
import random
import time
WIDTH = 1580
HEIGHT = 980
images = ["sword", "parrot", "hat", "ship"]

sounds.lofi.play(loops = -1)
start = time.time()
board = [["sword",None,None,"ship"],
         [None,"hat",None,None],
         [None,None,"parrot",None],
         [None,None,"ship",None]]

tile_w = WIDTH/4
tile_h = HEIGHT/4
selecter = None
currentactor = 0
gamestate = 0
#count = False
def stopsound() :
   sounds.incorrect.stop ()
def stopsound2() :
    sounds.good.stop()
def draw() :        
    screen.fill("white")
    if gamestate == 1 :
        screen.fill("red")
        screen.draw.text("game over",(0,0),fontsize = 50,color = "white")

    for i in range (4) :
        for j in range (4) :
            screen.draw.line((j*WIDTH/4,0),(j*WIDTH/4,HEIGHT),color="black")
            screen.draw.line((0,i*HEIGHT/4),(WIDTH,i*HEIGHT/4),color="black")
    for row in range(4) :
        for column in range(4) :
            if selecter == (row,column) :
                value = images[currentactor]

                if is_valid(row,column,value):
                    screen.draw.filled_rect(Rect((column * tile_w,row * tile_h),(tile_w,tile_h)),"green")
                    sounds.good.play()
                    clock.schedule(stopsound2,0.5)
                    

                else:
                    screen.draw.filled_rect(Rect((column * tile_w,row * tile_h),(tile_w,tile_h)),"red") 
                    sounds.incorrect.play()
                    clock.schedule(stopsound,0.5)

                

            


            if board[row][column] != None:
                p1 = Actor(board[row][column])
                p1.pos = (column * tile_w + tile_w/2,row * tile_h + tile_h /2)
                p1.opacity = 0.5  # Make images transparent
                p1.draw() 


def update():
    count = False
    global gamestate    
    for item in board :
        for sell in item :
            if sell == None :
                count = True
    if count == True :
        gamestate = 0
    else :
        gamestate = 1
    elapsed = time.time() - start
    if elapsed > 60 :
        gamestate = 1
            
            


def on_mouse_down(pos) :
    global selecter
    col = int(pos[0] // (WIDTH/4))
    row = int(pos[1] // (HEIGHT/4))
    print(col,row)
    if board[row][col] == None:
        selecter = (row,col)        
         
    else :
        selecter = None
def is_valid(row,col,value) :
    if value in board[row] :
        return False
    for i in range(4) :
        if board[i][col] == value:
            
            return False         
    return True
     
    
def on_key_down(key) :
    global images,currentactor,selecter,board,count,gamestate
    if selecter :
        row,col = selecter
        if key == keys.SPACE :
            value = images[currentactor]
            print(value) 
            if is_valid(row,col,value) :  
                board[row][col] = value
            currentactor = (currentactor + 1) % 4
    if key == keys.R :
        board = [["sword",None,None,"ship"],
         [None,"hat",None,None],
         [None,None,"parrot",None],
         [None,None,"ship",None]]
        currentactor = 0
        selecter = None
        count = False
        gamestate = 0


   


        

pgzrun.go()        
