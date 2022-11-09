from graphics import *
from Button import *

def main():


    win = GraphWin("ourButton", 500, 500)
    B = Button(win, Point(300, 100), Point(400, 175), "red", "Big Nose")
    B2 = Button(win, Point(300, 200), Point(400, 275), "blue", "Small Nose")

    bigNose = Polygon([Point(200, 200), Point(250, 300), Point(150, 300)])
    smallNose = Polygon([Point(200, 200), Point(220, 250), Point(180, 250)])

    for i in range(5):
        m = win.getMouse()

        if B.isClicked(m):
            smallNose.undraw()
            bigNose.undraw()
            bigNose.draw(win)
        if B2.isClicked(m):
            bigNose.undraw()
            smallNose.undraw()
            smallNose.draw(win)

if __name__ == "__main__":
    main()
