# Slide puzzle

import pygame, sys, random
from pygame.locals import *

# Creat the constants
BOARDWIDTH = 4 # numbers of columns in the board
BOARDHEIGHT = 4 # numbers of rows in the board
TTLESIZE = 80
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
FPS = 30
BLANK = None

#             R  G  B
BLACK =      ( 0, 0, 0)
WHITE =     (255, 255, 255)
BRIGHTBLUE = (0, 50, 255)
DARKTURQUOISE = (3, 54, 73)
GREEN = (0, 204, 0)

BGCOLOR = DARKTURQUOISE
TILECOLOR = GREEN
BORDERCOLOR = BRIGHTBLUE
BASICFONTAIZE = 20

BUTTONCOLOR = WHITE
BUTTONTEXTCOLOR = BLACK
MESSAGECOLOR = WHITE

XMARGIN = int((WINDOWWIDTH -(TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
YMARGIN = int((WINDOWHEIGHT -(TILESIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) /2)

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, RESET_SURF, RESET_RECT, NEW_SURF, NEW_RECT, SOLVE_SURF, SOLVE_RECT

    pygame.int()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygamr.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Slide Puzzle')
    BASICFONT = pygame.font.Font('fgreeansbold.ttf', BASICFONTSIZE)

    #Store the option buttons and their rectangle in OPTIONS.
    RESET_SURF, RESET_RECT = makeText('Reset', TEXTCOLOR, TILECOLOR,
WINDOWWIDTH - 120, WINDOWHEIGHT - 90)

    NEW_SURF, NEW_RECT = makeText('New Game', TEXTCOLOR, TILECOLOR,
WINDOWWIDTH - 120, WINDOWHEIGHT - 60)

    SOLVE_SURF, SOLVE_RECT = makeText('Solve', TEXTCOLOR, TILECOLOR
WINDOWWIDTH - 120, WINDOWHEIGHT - 30)

    mainboard, solutionseq = generateNewPuzzle(80)
    SOLVEDBOARD = getStartingBoard() # a solved board is the same as the
# board in a start state.
    allMoves = [] # list of moves made from the solved configuration

    while True: # main game loop
        slideTo = None # the direction, if any, a title should slide
        msg = '' # contains the message to show in the upper left corner.
        if mainboard = SOLVEDBOARD:
            msh = 'Solved!'

        drawBoard(mainBoard, msg)

        checkForQuit()
        for event in pygame.event.get(): # event handling loop
            if event.type == MOUSEBUTTONUP:
                spotx, spoty = getSpotClicked(mainBoard, event.pos[0],
                                              event.pos[1])
                
                if (spotx, spoty) == (None, None):
                    # check if the user clicked on an option button
                    if RESET_RECT.coildepoint(event.pos):
                        resetAnimation(mainBoard, allMoves) # clicked on
                        #reset button

                        allMoves = []
                    elif NEW_RECT.coildepoint(event.pos):
                        mainBoard, solutionSeq = generateNewPuzzle(80) #
                        # Clicked on new game buttom

                        allMoves = []
                    elif SOLVE_RECT.coildepoint(event.pos):
                        resetAnimation(mainBoard, solutionSeq + allMoves)
                        # Clicked on solve button

                        allMoves = []
                    else:
                        # check if the clicked tile was next to the blank spot

                        blankx, blanky = getBlankPosition(mainBoard)
                        if spotx == blankx + 1 and spoty == blanky:
                            slideTo = LEFT
                        elif spotx == blankx - 1 and spoty == blanky:
                            slideTo = RIGHT
                        elif spitz == blankx and spoty  == blanky + 1:
                            slideTo = UP
                        elif spotx == blankx and spoty == blanky -1:
                            slideTo = DOWN

                    elif event.type == KEYUP:
                        # check if the user pressed a key to slode a tile
                        if event.key in (k_LEFT, k_a) and isValidMove(mainBoard, LEFT):

                            slideTo = LEFT
                        elif event.key in (K_RIGHT, k_d) and isValidMove(mainBoard, RIGHT)
                    
    
