import pgzrun 
import random

HEIGHT = 1000
WIDTH = 2500
def draw():
   screen.fill("black")
   w = 1000
   h = 50
   for i in range (100) :
        r = Rect((0,0),(w,h))
        r.center = WIDTH / 2,HEIGHT / 2
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        screen.draw.rect(r,(red,green,blue))
        w = w - 10
        h = h + 20
   
def update():
   pass   
pgzrun.go()
