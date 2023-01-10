from graphics import *

class Fish:
    def __init__(self,img,pos,win):
        self.img = img
        self.x_pos = pos[0]*20+10
        self.y_pos = pos[1]*20+10
        self.win = win
        self.image = Image(Point(self.x_pos,self.y_pos),self.img)
        self.isAlive = True
    def draw(self):
        self.image.draw(self.win)

    def fish_move(self,x,y):
        f_x = x
        f_y = y
        if x<0 :
            f_x = 0
        if x>19:
            f_x = 19
        if y<0:
            f_y = 0
        if y>19:
            f_y = 19
            
        self.x_pos = f_x*20+10
        self.y_pos = f_y*20+10
        self.image = Image(Point(self.x_pos,self.y_pos),self.img)
        
    def undraw(self):
        self.image.undraw()
    def live(self):
        self.isAlive = True
    def die(self):
        self.isAlive = False

    def locate(self):
        return [(self.x_pos-10)/20,(self.y_pos-10)/20]

    def Alive(self):
        if self.isAlive == True:
            return True
        else:
            return False
