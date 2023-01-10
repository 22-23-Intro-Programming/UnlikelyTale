import time
import random
from Button import *
from graphics import *
from shark import *
from fish import *

win = GraphWin("Shark Simulator",600,600)
Fs1 = Fish("fish.png",[random.randint(0,19),random.randint(0,19)],win)
Sk = Shark("shark.png",[random.randint(0,19),random.randint(0,19)],win)


def Reset():
    Sk.undraw()
    Fs1.undraw()
    Fs1.die()

    Sk.shark_move(random.randint(0,19),random.randint(0,19))
    Fs1.fish_move(random.randint(0,19),random.randint(0,19))
    Fs1.live()

    Sk.draw()
    Fs1.draw()



def Try_Catch(fish):

    f_cd = fish.locate()
    s_cd = Sk.locate()
    k = Sk.try_chase(f_cd[0],f_cd[1])
    if k == "catch":
        Sk.undraw()
        Sk.shark_move(f_cd[0],f_cd[1])
        Sk.draw()
        fish.die()
        fish.undraw()
    ###
    elif k == "up_right":
        Sk.undraw()
        Sk.shark_move(s_cd[0]+1,s_cd[1]+2)
        Sk.draw()
        fish.fish_move(f_cd[0]+1,f_cd[1]+1)
        fish.draw()

    elif k == "right_up":
        Sk.undraw()
        Sk.shark_move(s_cd[0]+2,s_cd[1]+1)
        Sk.draw()
        fish.fish_move(f_cd[0]+1,f_cd[1]+1)
        fish.draw()
    ###
    elif k == "up_left":
        Sk.undraw()
        Sk.shark_move(s_cd[0]-1,s_cd[1]+2)
        Sk.draw()
        fish.fish_move(f_cd[0]-1,f_cd[1]+1)
        fish.draw()

    elif k == "left_up":
        Sk.undraw()
        Sk.shark_move(s_cd[0]-2,s_cd[1]+1)
        Sk.draw()
        fish.fish_move(f_cd[0]-1,f_cd[1]+1)
        fish.draw()

    ###
    elif k == "down_right":
        Sk.undraw()
        Sk.shark_move(s_cd[0]+1,s_cd[1]-2)
        Sk.draw()
        fish.fish_move(f_cd[0]+1,f_cd[1]-1)
        fish.draw()

    elif k == "right_down":
        Sk.undraw()
        Sk.shark_move(s_cd[0]+2,s_cd[1]-1)
        Sk.draw()
        fish.fish_move(f_cd[0]+1,f_cd[1]-1)
        fish.draw()

    ###
    elif k == "down_left":
        Sk.undraw()
        Sk.shark_move(s_cd[0]-1,s_cd[1]-2)
        Sk.draw()
        fish.fish_move(f_cd[0]-1,f_cd[1]-1)
        fish.draw()

    elif k == "left_down":
        Sk.undraw()
        Sk.shark_move(s_cd[0]-2,s_cd[1]-1)
        Sk.draw()
        fish.fish_move(f_cd[0]-1,f_cd[1]-1)
        fish.draw()

    ##
    elif k == "up":
        Sk.undraw()
        Sk.shark_move(s_cd[0],s_cd[1]+2)
        Sk.draw()
        fish.fish_move(f_cd[0]+1,f_cd[1]+1)
        fish.draw()     
    elif k == "down":
        Sk.undraw()
        Sk.shark_move(s_cd[0],s_cd[1]-2)
        Sk.draw()
        fish.fish_move(f_cd[0]-1,f_cd[1]-1)
        fish.draw()
    elif k == "left":
        Sk.undraw()
        Sk.shark_move(s_cd[0]-2,s_cd[1])
        Sk.draw()
        fish.fish_move(f_cd[0]-1,f_cd[1]-1)
        fish.draw()
    elif k == "right":
        Sk.undraw()
        Sk.shark_move(s_cd[0]+2,s_cd[1])
        Sk.draw()
        fish.fish_move(f_cd[0]+1,f_cd[1]+1)
        fish.draw()


def Move():
    
    Fs1.undraw()
    if Fs1.Alive() == True:
        Try_Catch(Fs1)




            
        



def main():


    
    for i in range(20):
        for j in range(20):
            sq = Rectangle(Point(i*20,j*20),Point(i*20+20,j*20+20))
            sq.draw(win)

    R = Button(win, Point(0,400), Point(200,450), "yellow", "Reset")
    Q = Button(win, Point(200,400), Point(400,450), "tomato", "Quit")
    M = Button(win, Point(0,450), Point(200,500), "cyan", "Move")
    Run = Button(win, Point(200,450), Point(400,500), "blue", "Run")

    Sk.draw()
    Fs1.draw()

    

 
    
    while True:
        m = win.getMouse()

        if R.isClicked(m):
            
            Reset()

        if M.isClicked(m):
            Move()
        if Run.isClicked(m):
            while True:
                if Fs1.Alive() != True:
                    break
                Move()
                time.sleep(0.5)
        if Q.isClicked(m):
            win.close()
            break
    
if __name__ == "__main__":
    main()

