import random
import numpy as np

class Minesweeper(object):
  def__init__(self)
    self.board = [[-1 for row in range(5)] for column in range(5)]
    self.addMines()
    self.stateSpace = [i for i in range(4**9)]
    self.actionSpace = {
      '1': (0,0),
      '2': (1,0),
      '3': (2,0),
      '4': (0,1),
      '5': (1,1),
      '6': (2,1),
      '7': (0,2),
      '8': (1,2),
      '9': (2,2)
    }
    self.actions = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    self.reward = 0
    self.clicks = 0
  
  def addMines(self):
    mineBoard = [[0 for row in range(5)] for column in range(5)]
    nmines = 0
    while nmines < 2:
      x = random.randint(1,3)
      y = random.randint(1,3)
      if mineBoard[x][y] == 0:
        mineBoard[x][y] = 1
        nmines += 1
    self.mines = mineBoard

  def is_done(self, board):
    for r in range(3):
      for c in range(3):
        if board[r][c] == -2:
          return True
    if self.clicks = 7:
      return True
    return False
  
  def setState(self, board):
    self.board = board

  def getBoard(self):
    return self.board

  def getState(self, board):
    state = ()
    for r in range(3):
      for c in range(3):
        state = state + (stateboard[r][c],)
    return state

  def click(self, state, action):
    self.board = openAdjacentBlocks(self.board, self.mines, action[0], action[1], action[0], action[1])
    self.reward += 1
    self.clicks += 1

    return getState(self.board), self.reward, is_done(self.board), None
  
  
  def adjacentCellsScore(board, x, y):
    score = 0
    for yi in range(y-1, y+2):
      if board[x-1][yi] == 1:
        score += 1
      if board[x][yi] == 1:
        score += 1
      if board[x+1][yi] == 1:
        score += 1

    return score

  def openAdjacentBlocks(board, mineboard, x, y, origx, origy):
    if board[x][y] != -1:
      return board
    if x == 0 or y == 0 or x == 4 or y == 4:
      return board
    
    if adjacentCellsScore(mineboard, x, y) == 0:
      board[x][y] = 0
      for yi in range(y-1, y+2):
        for xi in range(x-1, x+2):
          if xi != x or yi != y:
            board = openAdjacentBlocks(board, mineboard, xi, yi, origx, origy)
    else:
      board[x][y] = adjacentCellsScore(mineboard, x, y)
    return board

  def printBoard(board):
    for r in range(3, 0, -1):
      for c in range(1, 4):
        print(board[r][c], end = ' ')
      print()

# Your Algorithm goes here!
if __name__ == "__main__":
  
