import random

def Minesweeper():
  random.seed(0)
  win = 0
  board = [[0 for row in range(10)] for column in range(10)]

  mineBoard = board
  
  bombs = 0
  while bombs < 10:
    x = random.randint(1,8)
    y = random.randint(1,8)
    if mineBoard[x][y] == 0:
      mineBoard[x][y] = 1
      bombs += 1
  
  printBoard(mineBoard)

  while win == 1:
    score = 0
    x = input('X:')
    y = inpit('Y:')

    if mineBoard[x][y] == 1:
      print("L")
      print(score)
      quit()
    else:
      num = adjacentCellsScore(mineBoard, x, y)
      print(num)



def adjacentCellsScore(board, x, y):
  score = 0
  for yi in range(y-1, y+1):
    if board[x-1][yi] == 1:
      score += 1
    if board[x][yi] == 1:
      score += 1
    if board[x+1][yi] == 1:
      score += 1

  return score

def printBoard(board):
  for r in range(8):
    for c in range(8):
      print(board[r][c], end = ' ')
    print()

# Start of Program
if __name__ == "__main__":
  Minesweeper()
