import random

def Minesweeper():
  win = 0
  board = [[-1 for row in range(6)] for column in range(6)]

  mineBoard = [[0 for row in range(6)] for column in range(6)]
  
  bombs = 0
  while bombs < 3:
    x = random.randint(1,4)
    y = random.randint(1,4)
    if mineBoard[x][y] == 0:
      mineBoard[x][y] = 1
      bombs += 1

  while win == 0:
    printBoard(mineBoard)
    print()
    printBoard(board)
    score = 0
    y = int(input('X:'))
    x = int(input('Y:'))

    if mineBoard[x][y] == 1:
      print("L")
      print(score)
      quit()
    else:
      board = openAdjacentBlocks(board, mineBoard, x, y, x, y)



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
  if x == 0 or y == 0 or x == 5 or y == 5:
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
  for r in range(4, 0, -1):
    for c in range(1, 5):
      print(board[r][c], end = ' ')
    print()

# Start of Program
if __name__ == "__main__":
  Minesweeper()
