"""Memory, puzzle game of number pairs."""

from random import *
from turtle import *

from freegames import path
import numpy as np

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
# se crea variable np para contar taps
numTaps = 0

def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']
    global numTaps
    tilesclear = 0


    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
        tilesclear = tilesclear+1
        if tilesclear == 64:
            write("You won!",font=('Arial', 30, 'normal'))

    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

    
    numTaps+=1
    print("Número de Taps: "+str(numTaps))
        
def draw():
    """Draw image and tiles."""
    write("Número de Taps: "+str(numTaps),font=('Arial', 12, 'normal'),align = "right")
    clear()
    goto(0, 0)
    shape(car)
    stamp()
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        # se centró texto modificando valores sumados a x y y
        goto(x + 25, y+ 2)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'), align = "center")

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
