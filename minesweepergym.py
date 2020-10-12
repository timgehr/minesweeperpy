import random
import numpy as np

class Minesweeper(object):
  def __init__(self):
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
    self.takenActions = []
  
  def reset(self):
    self.board = [[-1 for row in range(5)] for column in range(5)]
    self.addMines()
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
    if self.clicks == 10:
      return True
    if self.reward == 7:
      return True
    return False
  
  def setState(self, board):
    self.board = board

  def getBoard(self):
    returnBoard = [[0 for i in range(3)] for j in range(3)]
    for r in range(3):
      for c in range(3):
        returnBoard[r][c] = self.board[r+1][c+1]
    return returnBoard

  def getState(self, board):
    state = ()
    for r in range(3):
      for c in range(3):
        state = state + (board[r][c],)
    return state

  def click(self, action):
    if self.mines[self.actionSpace[action][0]][self.actionSpace[action][1]] == 1:
      self.board[self.actionSpace[action][0]][self.actionSpace[action][1]] = -2
    elif action in self.takenActions:
      self.clicks += 1
    else:
      self.board = self.openAdjacentBlocks(self.board, self.mines, self.actionSpace[action][0], self.actionSpace[action][1], self.actionSpace[action][0], self.actionSpace[action][1])
      self.takenActions.append(self.actionSpace[action])
      self.reward += 1
      self.clicks += 1

    return self.board, self.reward, self.is_done(self.board), None
  
  def adjacentCellsScore(self, board, x, y):
    score = 0
    for yi in range(y-1, y+2):
      if board[x-1][yi] == 1:
        score += 1
      if board[x][yi] == 1:
        score += 1
      if board[x+1][yi] == 1:
        score += 1

    return score

  def openAdjacentBlocks(self, board, mineboard, x, y, origx, origy):
    if board[x][y] != -1:
      return board
    if x == 0 or y == 0 or x == 4 or y == 4:
      return board
    
    if self.adjacentCellsScore(mineboard, x, y) == 0:
      board[x][y] = 0
      for yi in range(y-1, y+2):
        for xi in range(x-1, x+2):
          if xi != x or yi != y:
            board = self.openAdjacentBlocks(board, mineboard, xi, yi, origx, origy)
    else:
      board[x][y] = self.adjacentCellsScore(mineboard, x, y)
    return board

  def printBoard(self, board):
    for r in range(3, 0, -1):
      for c in range(1, 4):
        print(board[r][c], end = ' ')
      print()
    print()

def getQ(Q, boardObs, action):
  return Q[boardObs[0][0]+1][boardObs[0][1]+1][boardObs[0][2]+1][boardObs[1][0]+1][boardObs[1][1]+1][boardObs[1][2]+1][boardObs[2][0]+1][boardObs[2][1]+1][boardObs[2][2]+1][action]

def bestAction(Q, obsrv, actions):
  QVal = np.array([getQ(Q, obsrv, action) for action in range(9)])
  best_action = np.argmax(QVal)
  return actions[best_action]

# Your Algorithm goes here!
if __name__ == "__main__":
  STEPSIZE = 0.1
  GAMMA = 0.95
  EPSILON = 1.0
  EPISODES = 50000
  REWARDS = [0 for i in range(EPISODES)]
  env = Minesweeper()

  Q_TABLE = [[[[[[[[[[0 #random.uniform(0,7)
  for a in range(9)] 
  for b in range(5)] 
  for c in range(5)] 
  for d in range(5)] 
  for e in range(5)] 
  for f in range(5)] 
  for g in range(5)] 
  for h in range(5)] 
  for i in range(5)]
  for j in range(5)]

  for episode in range(5):
    done = False
    obsrv = env.getBoard()
    state = env.getState(obsrv)

    while not done:
      randomval = random.random()
      randIndex = random.randint(0,8)
      if randomval < EPSILON:
        action = env.actions[randIndex]
      else:
        action = bestAction(Q_TABLE, obsrv, env.actions)

      obsrv_new, reward, done, debugg = env.click(action)
      env.printBoard(obsrv_new)
      action_new = bestAction(Q_TABLE, obsrv_new, env.actions)

      Q_old = getQ(Q_TABLE, obsrv, env.actions.index(action))
      Q_new = getQ(Q_TABLE, obsrv_new, env.actions.index(action_new))

      Q_TABLE[obsrv[0][0]+1][obsrv[0][1]+1][obsrv[0][2]+1][obsrv[1][0]+1][obsrv[1][1]+1][obsrv[1][2]+1][obsrv[2][0]+1][obsrv[2][1]+1][obsrv[2][2]+1][env.actions.index(action)] = Q_old + STEPSIZE*(reward + GAMMA*Q_new - Q_old)
      obsrv = obsrv_new
    
    if EPSILON - 1 / EPISODES >= 0:
      EPSILON -= 1 / EPISODES
    #if episode % 500 == 0:
      #print("This is run ", episode, ". The reward was ",reward)
    print("This is run ", episode, ". The reward was ",reward)
    
    REWARDS[episode] = reward
    env.reset()


