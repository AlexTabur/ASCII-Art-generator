import cv2 as cv
a=cv.imread("tranny hornyson.png")
a=cv.cvtColor(a, cv.COLOR_BGR2GRAY)

TileSize={'x':1, 'y':2}

def getChar(val):
    #chars="#%@$|;, "
    chars="█▓▒░"
    #chars="⠀⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿"
    #chars="⠂⠅⠪⠭⠯⠿"
    #n=len(chars)*(256-val)//256-1 #inverted
    n=len(chars)*val//256 #not inverted
    return chars[n]

def fill(x0, y0):
    summ=0
    for y in range(TileSize['y']):
        for x in range(TileSize['x']):
            summ+=a[y+y0-2][x+x0-2]
    summ=summ//(TileSize['x']*TileSize['y'])
    return getChar(summ)

text=""
for y in range(0, len(a)-TileSize['y'],TileSize['y']):
    for x in range(0, len(a[0])-TileSize['x'],TileSize['x']):
            text+=fill(x, y)
    text+="\n"

f=open("1.txt","w", encoding='utf-8')
f.write(text)
f.close()
