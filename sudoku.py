import pgzrun
import random
WIDTH = 1580
HEIGHT = 980
images = ["sword", "parrot", "hat", "ship"]



board = [["sword",None,None,"ship"],
         [None,"hat",None,None],
         [None,None,"parrot",None],
         [None,None,"ship",None]]

tile_w = WIDTH/4
tile_h = HEIGHT/4
selecter = None
currentactor = 0
def draw():
    screen.fill("white")

    for i in range (4) :
        for j in range (4) :
            screen.draw.line((j*WIDTH/4,0),(j*WIDTH/4,HEIGHT),color="black")
            screen.draw.line((0,i*HEIGHT/4),(WIDTH,i*HEIGHT/4),color="black")
    for row in range(4) :
        for column in range(4) :
            if board[row][column] != None:
                p1 = Actor(board[row][column])
                p1.pos = (column * tile_w + tile_w/2,row * tile_h + tile_h /2)
                p1.opacity = 0.5  # Make images transparent
                p1.draw() 



def update():    
    pass


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
    global images,currentactor,selecter,board
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

pgzrun.go()        