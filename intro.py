#!/usr/bin/pgzrun

import pgzrun
import pgzero
from ludzik import ludzik
from gra import game
from end import end


WIDTH = 1000
HEIGHT = 800

global gamemode
gamemode = game(WIDTH, HEIGHT)

def draw():
    gamemode.draw(screen)


def update():
    global gamemode
    nextMode = gamemode.update()

    if nextMode == None:
        return
    elif nextMode == 'goto_end':
       gamemode = end(WIDTH, HEIGHT)

pgzrun.go()