

from graphics import*

def main():
    
    win = GraphWin("My Circle", 800, 800)
    
    c1 = Circle(Point(50,50), 10)
    c2 = Circle(Point(750,50), 10)
    c3 = Circle(Point(50,750), 10)
    c4 = Circle(Point(750,750), 10)
    c5 = Circle(Point(400,400), 10)
    
    c1.draw(win)
    c2.draw(win)
    c3.draw(win)
    c4.draw(win)
    c5.draw(win)

    P = Point(200, 200)
    P.draw(win)

    L = Line(Point(100, 100), Point(600, 300))
    L.draw(win)

    R = Rectangle(Point(500,200), Point(300, 400))
    R.draw(win)

    T = Text(Point(400, 600), "Hello World!")
    T.draw(win)
    T.setSize(24)
    T.setStyle('bold')
    T.setTextColor('blue')

    E = Entry(Point(200, 700), 20)
    E.draw(win)




    
    p = win.getMouse() # Pause to view result
    print(p)
    win.close()    # Close window when done



if __name__ == "__main__":
    main()
