import cv2 as cv
a=cv.imread("ldn-dmon.png")
a=cv.cvtColor(a, cv.COLOR_BGR2GRAY)

TileSize={'x':16, 'y':32}

def fill(x, y):
    summ=0
    if a[y][x]==255:
        if a[y+31][x+15]==255:
            return "\\"
        else:
            return ">"
    if a[y][x+15]==255:
        if a[y+31][x]==255:
            return "/"
        else:
            return "<"

    i=0
    bruh=True
    while i<32 and bruh:
                if a[y+i][x+6]==0:
                    bruh=False
                i+=1
    if bruh:
        return "|"

    
    i=0
    bruh=True
    while i<19 and bruh:
                if a[y+i][x+6]==0:
                    bruh=False
                i+=1
    if bruh:
        return "!"
    i=0
    bruh=True
    while i<16 and bruh:
                if a[y+31][x+i]==0:
                    bruh=False
                i+=1
    if bruh:
        return "_"
    i=0
    bruh=True
    while i<16 and bruh:
                if a[y+15][x+i]==0:
                    bruh=False
                i+=1
    if bruh:
        return "-"
    if a[y+4][x+6]==255:
        if a[y+28][x+4]==255:
            return ";"
        elif a[y+20][x+6]==255:
            return ":"
        return "'"
    if a[y][x+2]==255:
        return "\""
    
    if a[y+20][x+6]==255:
        if a[y+28][x+4]==255:
            return ","
        else:
            return "."
    return " "
text=""
for y in range(0, len(a)-TileSize['y'],TileSize['y']):
    for x in range(0, len(a[0])-TileSize['x'],TileSize['x']):
            text+=fill(x, y)
    text+="\n"

f=open("1.txt","w", encoding='utf-8')
f.write(text)
f.close()
