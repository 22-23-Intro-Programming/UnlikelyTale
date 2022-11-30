from graphics import *
from Button import *

def main():

    win = GraphWin("Palindrome", 800, 600)
    win.setBackground("beige")

    Q = Button(win, Point(650, 500), Point(750, 575), "tomato", "QUIT")
    P = Button(win, Point(350, 350), Point(450, 425), "cyan", "Check!")

    E = Entry(Point(400, 300), 30)
    E.draw(win)

    T = Text(Point(400, 250), "Write something below that you think is a palindrome.")
    T.draw(win)

    M = Text(Point(411, 522), "Answer in going to appear right here:")
    M.draw(win)

    while True:
        m = win.getMouse()

        if Q.isClicked(m):
            break

        if P.isClicked(m):
            pal = E.getText()
    
            start = pal[0]
            last = len(pal)-1
            i = 0
            for char in pal:
                if (pal[i] != pal[last-i]):
                    M.setText(":v This isn't a palindrome :v")
                    break
                i = i + 1
                M.setText(":v This is a palindrome :v ")


            #test pal for palindrome
            #have a GUI output for the result

    win.close()
        


if __name__ == "__main__":
    main()
