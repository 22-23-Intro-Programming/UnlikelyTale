from graphics import *
from Button import *

def main():
    win = GraphWin("Character Creator", 800, 800)
    Face = Oval(Point(75, 100), Point(475, 700))
    Face.draw(win)
#button:
    eyes1 = Button(win, Point(580, 100), Point(660, 175), "green", "Square Eyes")
    eyes2 = Button(win, Point(705, 100), Point(785, 175), "green", "Small Eyes")
    nose1 = Button(win, Point(580, 200), Point(660, 275), "yellow", "Big Nose")
    nose2 = Button(win, Point(705, 200), Point(785, 275), "yellow", "Small Nose")
    ears1 = Button(win, Point(580, 300), Point(660, 375), "blue", "Round Ears")
    ears2 = Button(win, Point(705, 300), Point(785, 375), "blue", "Square Ears")
    mouth1 = Button(win, Point(580, 400), Point(660, 475), "cyan", "Happy Mouth")
    mouth2 = Button(win, Point(705, 400), Point(785, 475), "cyan", "Normal Mouth")

#parts:
    be1 = Rectangle(Point(155, 200), Point(255, 275))
    be2 = Rectangle(Point(295, 200), Point(395, 275))
    se1 = Oval(Point(175, 200), Point(225, 275))
    se2 = Oval(Point(325, 200), Point(375, 275))

    bn = Polygon(Point(275, 275), Point(225, 400), Point(325, 400))
    sn = Polygon(Point(275, 320), Point(250, 375), Point(300, 375))

    re1 = Circle(Point(510, 350), 39)
    re2 = Circle(Point(40, 350), 39)
    sqe1 = Rectangle(Point(475, 300), Point(535, 450))
    sqe2 = Rectangle(Point(75, 300), Point(15, 450))

    hm = Polygon(Point(118, 480), Point(283, 550), Point(438, 480))
    nm = Line(Point(200, 525), Point(360, 525))
#Quit:
    QButton = Button(win, Point(550, 675), Point(775, 725), "red", "Quit!")

#lists
    eyes = [be1, be2, se1, se2]
    nose = [bn, sn]
    ears = [re1, re2, sqe1, sqe2]
    mouth = [hm, nm]
    
#while loop
    while True:
        m = win.getMouse()
        
        if eyes1.isClicked(m):
            se1.undraw()
            se2.undraw()
       
            be1.draw(win)
            be2.draw(win)

        elif eyes2.isClicked(m):
            be1.undraw()
            be2.undraw()
         
            se1.draw(win)
            se2.draw(win)

        elif nose1.isClicked(m):
            sn.undraw()
            bn.undraw()
            bn.draw(win)

        elif nose2.isClicked(m):
            bn.undraw()
            sn.undraw()
            sn.draw(win)

        elif ears1.isClicked(m):
            sqe1.undraw()
            sqe2.undraw()
         
            re1.draw(win)
            re2.draw(win)

        elif ears2.isClicked(m):
            re1.undraw()
            re2.undraw()
            
            sqe1.draw(win)
            sqe2.draw(win)

        elif mouth1.isClicked(m):
            nm.undraw()
            hm.undraw()
            hm.draw(win)

        elif mouth2.isClicked(m):
            hm.undraw()
            nm.undraw()
            nm.draw(win)


        elif QButton.isClicked(m):
            break

        
    win.close()

if __name__ == "__main__":
    main()
