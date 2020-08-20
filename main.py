import pygame as pygame
pygame.init()
import os
import math
import random as random

WIN_HEIGHT = 800
WIN_WIDTH = 640

BLOCK_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join(str(x) + ".png"))) for x in range(0,3)]
BGD = pygame.image.load(os.path.join("bgd.png"))
STAT_FONT = pygame.font.SysFont("comicsans", 50)

#see if player can put piece there or not
def canPlace(shape, board, x, y):
        if shape == "1x1":
            if board[y][x] == 1:
                return False
            else:
                return True
        elif shape == "2x2":
            if x*y > 0:
                p = board[y][x] + board[y][x-1] + board[y-1][x] + board[y-1][x-1]
                if p != 0:
                    return False
                else:
                    return True
            else:
                return False
        elif shape == "3x3":
            if (x > 1) and (y>1):
                p = board[y][x] + board[y][x-1] + board[y-1][x] + board[y-1][x-1] + board[y-2][x] + board[y][x-2] + board[y-2][x-2] + board[y-1][x-2] + board[y-2][x-1]
                if p != 0:
                    return False
                else:
                    return True
            else:
                return False
        elif shape == "H2":
            if (x > 0):
                p = board[y][x]+board[y][x-1]
                if p != 0:
                    return False
                else:
                    return True
            else:
                return False
        elif shape == "H3":
            if (x > 1):
                p = board[y][x]+board[y][x-1]+board[y][x-2]
                if p != 0:
                    return False
                else:
                    return True
            else:
                return False
        elif shape == "H4":
            if (x > 2):
                p = board[y][x]+board[y][x-1]+board[y][x-2]+board[y][x-3]
                if p != 0:
                    return False
                else:
                    return True
            else:
                return False
        elif shape == "H5":
            if (x > 3):
                p = board[y][x]+board[y][x-1]+board[y][x-2]+board[y][x-3]+board[y][x-4]
                if p != 0:
                    return False
                else:
                    return True
            else:
                return False
        elif shape == "V2":
            if (y > 0):
                p = board[y][x]+board[y-1][x]
                if p != 0:
                    return False
                else:
                    return True
            else:
                return False
        elif shape == "V3":
            if (y > 1):
                p = board[y][x]+board[y-1][x]+board[y-2][x]
                if p != 0:
                    return False
                else:
                    return True
            else:
                return False
        elif shape == "V4":
            if (y > 2):
                p = board[y][x]+board[y-1][x]+board[y-2][x]+board[y-3][x]
                if p != 0:
                    return False
                else:
                    return True
            else:
                return False
        elif shape == "V5":
            if (y > 3):
                p = board[y][x]+board[y-1][x]+board[y-2][x]+board[y-3][x]+board[y-4][x]
                if p != 0:
                    return False
                else:
                    return True
            else:
                return False
        elif shape == "SL1":
            if (y > 0) and (x<9):
                p = board[y][x]+board[y-1][x]+board[y][x+1]
                if p != 0:
                    return False
                else:
                    return True
            else:
                return False
        elif shape == "BL1":
            if (y > 1) and (x<8):
                p = board[y][x]+board[y-1][x]+board[y][x+1]+board[y-2][x]+board[y][x+2]
                if p != 0:
                    return False
                else:
                    return True
            else:
                return False
        elif shape == "SL2":
            if (y > 0) and (x>0):
                p = board[y][x]+board[y-1][x]+board[y][x-1]
                if p != 0:
                    return False
                else:
                    return True
            else:
                return False
        elif shape == "BL2":
            if (y > 1) and (x>1):
                p = board[y][x]+board[y-1][x]+board[y][x-1]+board[y-2][x]+board[y][x-2]
                if p != 0:
                    return False
                else:
                    return True
            else:
                return False
        elif shape == "SL3":
            if (y < 9) and (x>0):
                p = board[y][x]+board[y+1][x]+board[y][x-1]
                if p != 0:
                    return False
                else:
                    return True
            else:
                return False
        elif shape == "BL3":
            if (y < 8) and (x>1):
                p = board[y][x]+board[y+1][x]+board[y][x-1]+board[y+2][x]+board[y][x-2]
                if p != 0:
                    return False
                else:
                    return True
            else:
                return False
        elif shape == "SL4":
            if (y <9) and (x<9):
                p = board[y][x]+board[y+1][x]+board[y][x+1]
                if p != 0:
                    return False
                else:
                    return True
            else:
                return False
        elif shape == "BL4":
            if (y < 8) and (x<8):
                p = board[y][x]+board[y+1][x]+board[y][x+1]+board[y+2][x]+board[y][x+2]
                if p != 0:
                    return False
                else:
                    return True
            else:
                return False
        
#class for the game
class Board(object):

    board = []
    SIZE = 10
    WIDTH = 64

    def __init__(self):
        #creates a 10x10 board, fills array with 0
        for i in range(self.SIZE):
            tmp = []
            for j in range(self.SIZE):
                tmp.append(0)
            self.board.append(tmp)
        self.board[9][0] = 1

    #draw function, draws different color dependeing on score
    def draw(self, win):
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if self.board[i][j] == 0:
                    win.blit(BLOCK_IMGS[0], (j*self.WIDTH, i*self.WIDTH))
                elif self.board[i][j] == 1:
                    win.blit(BLOCK_IMGS[1], (j*self.WIDTH, i*self.WIDTH))

    #helper function
    def getBlock(self, y, x):
        return self.board[y][x]
    
    #places block depending on which piece it is
    def invert(self,shape, y, x):
        if shape == "1x1":
            self.board[y][x] =1 
        elif shape == "2x2":
            self.board[y][x] =1
            self.board[y-1][x] =1 
            self.board[y][x-1] =1 
            self.board[y-1][x-1] =1 
        elif shape == "3x3":
            self.board[y][x] =1
            self.board[y-1][x] =1 
            self.board[y][x-1] =1 
            self.board[y-1][x-1] =1 
            self.board[y-2][x] =1 
            self.board[y][x-2] =1 
            self.board[y-2][x-2] =1 
            self.board[y-2][x-1] =1 
            self.board[y-1][x-2] =1 
        elif shape == "H2":
            self.board[y][x] =1
            self.board[y][x-1] =1
        elif shape == "H3":
            self.board[y][x] =1
            self.board[y][x-1] =1
            self.board[y][x-2] =1
        elif shape == "H4":
            self.board[y][x] =1
            self.board[y][x-2] =1
            self.board[y][x-1] =1
            self.board[y][x-3] =1
        elif shape == "H5":
            self.board[y][x] =1
            self.board[y][x-1] =1
            self.board[y][x-2] =1
            self.board[y][x-4] =1
            self.board[y][x-3] =1
        elif shape == "V2":
            self.board[y][x] =1
            self.board[y-1][x] =1
        elif shape == "V3":
            self.board[y][x] =1
            self.board[y-1][x] =1
            self.board[y-2][x] =1
        elif shape == "V4":
            self.board[y][x] =1
            self.board[y-1][x] =1
            self.board[y-2][x] =1
            self.board[y-3][x] =1
        elif shape == "V5":
            self.board[y][x] =1
            self.board[y-1][x] =1
            self.board[y-2][x] =1
            self.board[y-3][x] =1
            self.board[y-4][x] =1
        elif shape == "SL1":
            self.board[y][x] =1
            self.board[y-1][x] =1
            self.board[y][x+1] =1
        elif shape == "SL2":
            self.board[y][x] =1
            self.board[y-1][x] =1
            self.board[y][x-1] =1
        elif shape == "SL3":
            self.board[y][x] =1
            self.board[y+1][x] =1
            self.board[y][x-1] =1
        elif shape == "SL4":
            self.board[y][x] =1
            self.board[y+1][x] =1
            self.board[y][x+1] =1
        elif shape == "BL1":
            self.board[y][x] =1
            self.board[y-1][x] =1
            self.board[y][x+1] =1
            self.board[y-2][x] =1
            self.board[y][x+2] =1
        elif shape == "BL2":
            self.board[y][x] =1
            self.board[y-1][x] =1
            self.board[y][x-1] =1
            self.board[y-2][x] =1
            self.board[y][x-2] =1
        elif shape == "BL3":
            self.board[y][x] =1
            self.board[y+1][x] =1
            self.board[y][x-1] =1
            self.board[y+2][x] =1
            self.board[y][x-2] =1
        elif shape == "BL4":
            self.board[y][x] =1
            self.board[y+1][x] =1
            self.board[y][x+1] =1
            self.board[y+2][x] =1
            self.board[y][x+2] =1

    #checks if any of the rows are completed
    def checkRow(self):
        res = []
        for y in range(10):
            p = 1
            for x in range(10):
                p*=self.board[y][x]
            if p==1:
                res.append(y)
        return res

    #checks if any columns are completed
    def checkColumn(self):
        res = []
        for x in range(10):
            p = 1
            for y in range(10):
                p*=self.board[y][x]
            if p==1:
                res.append(x)
        return res

    #if a row is completed, it sets it to normal
    def invertRows(self, rows):
        for row in rows:
            for x in range(10):
                self.board[row][x] = 0

    #if a column is completed, it sets it to normal
    def invertColumns(self, columns):
        for column in columns:
            for y in range(10):
                self.board[y][column] = 0

    #helper function to return what the board is
    def returnMap(self):
        return self.board

#---------------------------------------------------------------------------------

#class for other ai implementation
class Block(object):

    def __init__(self, y, x, state):
        self.x = x
        self.y = y
        self.state = state
    
    def change(self, newState):
        self.state = newState

    def getState(self):
        return self.state

def updateBlocks(board, blocks):
    for i in range(10):
        for j in range(10):
            blocks[i][j].change(board.getBlock(i, j))

#-----------------------------------------------------------------------------------

#main
def main():

    #used of ai later
    blocks = []

    for i in range(10):
        tmp = []
        for j in range(10):
            tmp.append(Block(i,j,0))
        blocks.append(tmp)

    #inits board and game
    board = Board()
    clock = pygame.time.Clock()
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    #creates game variables
    inv = fillInv()
    score = 0
    nextPiece = ""

    #game loop
    run = True
    while run:
        clock.tick(30)
        #event loop
        for event in pygame.event.get():
            #quiting game
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                break

            #selecting piece to play
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    nextPiece = inv[0]
                elif event.key == pygame.K_2:
                    nextPiece = inv[1]
                elif event.key == pygame.K_3:
                    nextPiece = inv[2]

            #placing piece
            elif event.type == pygame.MOUSEBUTTONUP:
                #grabs mouse pos
                pos = pygame.mouse.get_pos()
                x, y = pos[0]//64, pos[1]//64
                if x > 9:
                    x = 9
                if y > 9:
                    y = 9

                #checks if it fits, if so place    
                if canPlace(nextPiece, board.returnMap(), x, y):
                    board.invert(nextPiece,y,x)
                    if nextPiece != '':
                        #adds score
                        score += pieceScore(nextPiece)
                        inv.remove(nextPiece)

        #fills inv if its empty
        if len(inv) ==0:
            inv = fillInv()

        #checks if game is over or not
        tmp = 0
        for b in inv:
            for y in range(10):
                for x in range(10):
                    if canPlace(b, board.returnMap(), x, y):
                        tmp+=1
                        break
        if tmp == 0:
            run = False


        #checks if any rows are completed
        col = board.checkColumn()
        row = board.checkRow()

        num = len(row) + len(col)
        score += countScore(num)

        board.invertColumns(col)
        board.invertRows(row)

        #used for ai integration
        updateBlocks(board, blocks)
        
        #draw
        draw_window(win,board,score,inv)
    pygame.quit()

#-------------------------------------------------------------------------------------------

#helper function for adjusting score
def pieceScore(shape):
    shapes = {"1x1":1, "2x2":4, "3x3":9, "H2":2, "H3":3, "H4":4, "H5":5, "V2":2,"V3":3,"V4":4,"V5":5,"SL1":3,"SL2":3,"SL3":3,"SL4":3,"BL1":5,"BL2":5,"BL3":5,"BL4":5}
    return shapes[shape]
    
#helper function to fill player inv
def fillInv():
    shapes = ["1x1", "2x2", "3x3", "H2", "H3", "H4", "H5", "V2","V3","V4","V5","SL1","SL2","SL3","SL4","BL1","BL2","BL3","BL4"]
    inv = []
    for j in range(3):
        i = int(random.random()*(len(shapes)-1))
        inv.append(shapes[i])
    return inv

#helper function to figure out score
def countScore(n):
    if n == 0:
        return 0
    elif (n == 1) or (n==2):
        return n*10
    elif n==3:
        return n*13
    elif n==4:
        return n*25
    elif n>=5:
        return n*40

#------------------------------------------------------------------------------------

#draw
def draw_window(win, board, score, inv):

    win.blit(BGD, (0,0))

    board.draw(win)

    score_ = STAT_FONT.render("Score: " + str(score), 1, (255,255,255))
    win.blit(score_, (10, 660))

    piece_ = STAT_FONT.render("Inventory: " + str(inv), 1, (255,255,255))
    win.blit(piece_, (10, 700))

    pygame.display.update()



#call game
main()