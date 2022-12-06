from graphics import*
from Button import*

def darken(img):

    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i,j)
            r, g, b = pix[0], pix[1], pix[2]
            if r > 100:
                r = r - 100
            else:
                r = 0
            if g > 100:
                g = g - 100
            else:
                g = 0
            if b > 100:
                b = b - 100
            else:
                b = 0
            
            dColor = color_rgb(r,g,b)
            img.setPixel(i, j, dColor)
def lighten(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i,j)
            r, g, b = pix[0], pix[1], pix[2]
            if r < 225:
                r = r + 30
            else:
                r = 255
            if g < 225:
                g = g + 30
            else:
                g = 255
            if b < 225:
                b = b + 30
            else:
                b = 255
            
            lColor = color_rgb(r,g,b)
            img.setPixel(i, j, lColor)
def grayscale(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            gray = r + b + g
            gray = gray // 3

            gColor = color_rgb(gray, gray, gray)
            img.setPixel(i, j, gColor)

def contrast(img):
    x = img.getWidth()
    y = img.getHeight()
    

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]
            avg = r + g + b
            avg = avg // 3
            if avg > 128:
                if r < 225:
                    r = r + 30
                else:
                    r = 255
                if g < 225:
                    g = g + 30
                else:
                    g = 255
                if b < 225:
                    b = b + 30
                else:
                    b = 255

            elif avg < 128:
                if r > 100:
                    r = r - 100
                else:
                    r = 0
                if g > 100:
                    g = g - 100
                else:
                    g = 0
                if b > 100:
                    b = b - 100
                else:
                    b = 0
         

            

            
            cColor = color_rgb(r,g,b)
            img.setPixel(i, j,cColor)
def main():

    win = GraphWin("Image Editor", 800, 600)
    win.setBackground("#FFAA00")

    I = Image(Point(300, 300), "veitchii.png")
    I.draw(win)

    B = Button(win, Point(600, 100), Point(700, 175), "tomato", "Darken")
    B2 = Button(win, Point(600, 200), Point(700, 275), "tomato", "Lighten")
    B3 = Button(win, Point(600, 300), Point(700, 375), "tomato", "Grayscale")
    B4 = Button(win, Point(600, 400), Point(700, 475), "tomato", "contrast")
    Q = Button(win, Point(600, 590), Point(700, 555), "misty rose", "QUIT")

    while True:
        m = win.getMouse()
        
        if B.isClicked(m):
            darken(I)
        if B2.isClicked(m):
            lighten(I)
        if B3.isClicked(m):
            grayscale(I)
        if B4.isClicked(m):
            contrast(I)

        if Q.isClicked(m):
            break

    win.close()

if __name__ == "__main__":
    main()
