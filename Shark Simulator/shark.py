from graphics import *

class Shark:
    def __init__(self,img,pos,win):
        self.img = img
        self.x_pos = pos[0]*20+10
        self.y_pos = pos[1]*20+10
        self.win = win
        self.image = Image(Point(self.x_pos,self.y_pos),self.img)

    def draw(self):
        self.image.draw(self.win)

    def shark_move(self,x,y):
        s_x = x
        s_y = y
        if x<0:
            s_x = 0
        if x>19:
            s_x = 19
        if y<0:
            s_y = 0
        if y>19:
            s_y = 19
        
        
        self.x_pos = s_x*20+10
        self.y_pos = s_y*20+10
        self.image = Image(Point(self.x_pos,self.y_pos),self.img)
    def undraw(self):
        self.image.undraw()

    def locate(self):
        return [(self.x_pos-10)/20,(self.y_pos-10)/20]


    def try_chase(self,x,y):
        s_x = (self.x_pos-10)/20
        s_y = (self.y_pos-10)/20
        if ((s_x-x)**2+(s_y-y)**2) < 8:
            return "catch"
        elif x-s_x == 0 and s_y-y > 0:
            return "down"
        elif x-s_x == 0 and s_y-y < 0:
            return "up"
        elif y-s_y == 0 and s_x-x > 0:
            return "left"
        elif y-s_y == 0 and s_y-y < 0:
            return "right"

        #Shark goes down-left
        elif (s_x-x) > 0 and (s_y-y) > 0 and abs(x-s_x) >= abs(s_y-y):
            return "left_down"
        elif (s_x-x) > 0 and (s_y-y) > 0 and abs(x-s_x) <= abs(s_y-y):
            return "down_left"
        
        #Shark goes up_left
        elif (s_x-x) > 0 and (s_y-y) < 0 and abs(x-s_x) >= abs(s_y-y):
            return "left_up"
        elif (s_x-x) > 0 and (s_y-y) < 0 and abs(x-s_x) <= abs(s_y-y):
            return "up_left"

        #Shark goes down-right
        elif (s_x-x) < 0 and (s_y-y) > 0 and abs(x-s_x) >= abs(s_y-y):
            return "right_down"
        elif (s_x-x) < 0 and (s_y-y) > 0 and abs(x-s_x) <= abs(s_y-y):
            return "down_right"
        
        #Shark goes up_right
        elif (s_x-x) < 0 and (s_y-y) < 0 and abs(x-s_x) >= abs(s_y-y):
            return "right_up"
        elif (s_x-x) < 0 and (s_y-y) < 0 and abs(x-s_x) <= abs(s_y-y):
            return "up_right"
              



        
            
        

    
