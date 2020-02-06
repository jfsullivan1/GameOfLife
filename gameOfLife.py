#Game of Life
#John Sullivan & Sofia Rossi & William Ross
#CSC 310
#1/29/2020

import os
import time
import random
import sys
import copy

def displayArray(ar):
    os.system('clear')

    rows = len(ar)

    if rows == 0:
        raise ValueError("Array contains no data")

    cols = len(ar[0])

    for i in range(rows):
        for j in range(cols):
            print(ar[i][j],end=' ')
        print()

    time.sleep(1)


class Game:
    def makeBoard(boardWidth, boardHeight, numGens):
        board = []
        for i in range(boardHeight):
            newRow = []
            for j in range(boardWidth):
                randCell = random.randint(0, 1)
                if (randCell == 0):
                    newRow.append(' ')
                else:
                    newRow.append('*')
                if (j == ((boardWidth) - 1)):
                    board.append(newRow)
        return board
    
    def checkNeighbors(board, i, j):
        liveCellCount = 0
        if (i+1 < len(board) - 1):
            if(board[i+1][j] == '*'):
                liveCellCount+=1
        if (i+1 < len(board) - 1 and j+1 < len(board[i]) - 1):
            if (board[i+1][j+1] == '*'):
                liveCellCount+=1
        if (j+1 < len(board) - 1):
            if(board[i][j+1] == '*'):
                liveCellCount+=1
        if (i != 0 and j+1 < len(board[i]) - 1):
            if(board[i-1][j+1] == '*'):
                liveCellCount+=1
        if (i != 0):
            if(board[i-1][j] == '*'):
                liveCellCount+=1
        if (i != 0 and j != 0):
            if (board[i-1][j-1] == '*'):
                liveCellCount+=1
        if (j != 0):
            if(board[i][j-1] == '*'):
                liveCellCount+=1
        if (j != 0 and i < len(board) - 1):
            if(board[i+1][j-1] == '*'):
                liveCellCount+=1
            
        return liveCellCount
        
    def nextGen(board):
        #Any live cell with fewer than two live neighbors dies  
        #Any live cell with two or three live neighbors lives on to the next genertaio
        #Any live cell with more than three live neighbors dies, as if by overpopulation
        #Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction
        for i in range(len(board)):
            for j in range(len(board[i])):
                liveCellCount = Game.checkNeighbors(board, i, j)
                if (liveCellCount < 2):
                    if (board[i][j] == '*'):
                        board[i][j] = ' '
                if (liveCellCount > 3):
                    if (board[i][j] == '*'):
                        board[i][j] = ' '
                if (liveCellCount == 3):
                    if (board[i][j] == ' '):
                        board[i][j] = '*'
        return board

            
                       
        
def startGame(boardWidth, boardHeight, numGens):
    board = Game.makeBoard(boardWidth, boardHeight, numGens)
    secondBoard = copy.deepcopy(board) 
    displayArray(board)
    i = 0
    while i < numGens:
        board = Game.nextGen(secondBoard)
        secondBoard = copy.deepcopy(board)
        displayArray(board)
        i+=1

def getDimensionsFromUser():
    print("====================")
    print("    Game of Life    ")
    print("====================")

    boardWidth = int(input("Please enter a board width: "))
    boardHeight = int(input("Please enter a board height: "))
    numGens = int(input("Please enter the number of generations: "))

    return boardWidth, boardHeight, numGens
                
def main():
    boardWidth, boardHeight, numGens = getDimensionsFromUser()
    startGame(boardWidth, boardHeight, numGens)
    
                
main()         
            
