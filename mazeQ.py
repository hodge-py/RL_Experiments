import numpy as np
import random
import math
import matplotlib.pyplot as plt
import sys

"""
epilson = 0
qTable = np.zeros((100,4))
print(qTable)

for i in range(1000):
  epilson = epilson + (-.01)
  eValue = math.e ** (epilson)
  curState = 0
  r = 0
  s = 0
  tuples = []
"""
"""
  for y in range(100):
    randVal = random.random()
    if randVal > eValue: #exploitative action
      intRand = qTable[curState].argmax()


      if s == 2 and r == 2:
        qTable[curState][intRand] = qTable[curState][intRand] + .1 * (1 + .99*qTable[curState+1].max() - qTable[curState][intRand])
        break
      elif (s,r) in tuples:
          qTable[curState][intRand] = qTable[curState][intRand] + .1 * (-.1 + .99*qTable[curState+1].max() - qTable[curState][intRand])
      else:
        qTable[curState][intRand] = qTable[curState][intRand] + .1 * (0 + .99*qTable[curState+1].max() - qTable[curState][intRand])

      curState += 1

    else: # random action
      intRand = random.randint(0,3)


      if s == 2 and r == 2:
        qTable[curState][intRand] = qTable[curState][intRand] + .1 * (1 + .99*qTable[curState+1].max() - qTable[curState][intRand])
        break
      elif (s,r) in tuples:
          qTable[curState][intRand] = qTable[curState][intRand] + .1 * (-.1 + .99*qTable[curState+1].max() - qTable[curState][intRand])
      else:
        qTable[curState][intRand] = qTable[curState][intRand] + .1 * (0 + .99*qTable[curState+1].max() - qTable[curState][intRand])
"""


masterArr = np.array([
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
[1, 1, 0, 0, 0, 0, 1, 0, 0, 0],
[0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
[1, 1, 1, 1, 1, 0, 0, 1, 0, 0],
[0, 0, 1, 0, 0, 0, 0, 1, 1, 1],
[0, 0, 1, 0, 0, 1, 1, 1, 0, 0],
[0, 0, 1, 0, 0, 1, 1, 0, 1, 0],
[0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
[0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
[0, 0, 0, 0, 1, 1, 1, 0, 0, 0]])

masterArr2 = np.array([
[0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
[0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
[0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
[0, 1, 1, 0, 0, 0, 0, 0, 1, 1],
[0, 1, 1, 1, 0, 1, 1, 0, 1, 1],
[0, 0, 0, 0, 0, 1, 1, 0, 0, 0]])
 
print(masterArr.shape)
#maze = plt.imshow(masterArr)
#plt.show()

class MazeSolver:

  def __init__(self, maze):
    self.maze = maze
    self.size = maze.shape[0]
    self.curState = 0
    self.qTable = 0
    self.y = 0
    self.x = 0
    self.minReward = -7
    self.preC = []
  
  def reward(self):
    rewardVal = {
      "valid": 0,
      "invalid": -.4,
      "repeat": -.1,
      "complete": 5
    }
    return rewardVal

  def movement(self,boolean):
    moves = [0,1,2,3]
    # record the coordinate
    choices = 0
    valid = False
    counter = 0
    

    while valid == False:
      if boolean:
        choices = random.choice(moves)
      #print(choices)
      else:
        choices = self.qTable[self.curState].argmax()

      if choices == 0:
        if self.y - 1 < 0:
          #invalid
          pass
        elif self.y > 0 and self.maze[self.x][self.y-1] == 1:
          pass
        elif (self.x,self.y-1) in self.preC:
          self.y -= 1
          self.qTable[self.curState][choices] = self.qTable[self.curState][choices] + .1*(self.reward()["repeat"] + .99*self.qTable[self.curState+1].max() - self.qTable[self.curState][choices])
          valid = True
          #print("repeat",self.x,self.y)
        else:
          self.y -= 1
          valid = True
          self.qTable[self.curState][choices] = self.qTable[self.curState][choices] + .1*(self.reward()["valid"] + .99*self.qTable[self.curState+1].max() - self.qTable[self.curState][choices])

      if choices == 1:
        if self.y+1 > self.size-1:
          pass
        elif self.y < self.size-1 and self.maze[self.x][self.y+1] == 1:
          pass
        elif (self.x,self.y+1) in self.preC:
          self.qTable[self.curState][choices] = self.qTable[self.curState][choices] + .1*(self.reward()["repeat"] + .99*self.qTable[self.curState+1].max() - self.qTable[self.curState][choices])
          self.y += 1
          valid = True
        else:
          self.y += 1
          self.qTable[self.curState][choices] = self.qTable[self.curState][choices] + .1*(self.reward()["valid"] + .99*self.qTable[self.curState+1].max() - self.qTable[self.curState][choices])
          valid = True


      if choices == 2:
        if self.x-1 < 0:
          #invalid
          pass
        elif self.x > 0 and self.maze[self.x - 1][self.y] == 1:
          pass
        elif (self.x-1,self.y) in self.preC:
          valid = True
          self.x -= 1
          self.qTable[self.curState][choices] = self.qTable[self.curState][choices] + .1*(self.reward()["repeat"] + .99*self.qTable[self.curState+1].max() - self.qTable[self.curState][choices])
        else:
          valid = True
          self.x -= 1
          self.qTable[self.curState][choices] = self.qTable[self.curState][choices] + .1*(self.reward()["valid"] + .99*self.qTable[self.curState+1].max() - self.qTable[self.curState][choices])

      if choices == 3:
        if self.x+1 > self.size-1:
          pass
        elif self.maze[self.x+1][self.y] == 1:
          pass
        elif (self.x+1,self.y) in self.preC:
          valid = True
          self.x += 1
          self.qTable[self.curState][choices] = self.qTable[self.curState][choices] + .1*(self.reward()["repeat"] + .99*self.qTable[self.curState+1].max() - self.qTable[self.curState][choices])
        else:
          valid = True
          self.x += 1
          self.qTable[self.curState][choices] = self.qTable[self.curState][choices] + .1*(self.reward()["valid"] + .99*self.qTable[self.curState+1].max() - self.qTable[self.curState][choices])

      counter += 1

      if counter > 4:
        self.qTable[self.curState][choices] = self.qTable[self.curState][choices] + .1*(self.reward()["invalid"] + .99*self.qTable[self.curState+1].max() - self.qTable[self.curState][choices])
        #print("invalidd")
        return "error"

    return choices
    


  def mainRun(self):
    self.qTable = np.zeros(((self.size*self.size),4))
    epilson = 0
    for i in range(100000):
      epilson = epilson + (-.001)
      eValue = math.e ** (epilson)
      self.curState = 0
      self.preC = []
      self.x = 0
      self.y = 0
      self.secondaryLoop(eValue)

    print(self.qTable)
    store = []
    for x in range(len(self.qTable)):
      print(self.qTable[x].argmax())

  def secondaryLoop(self,epi):
    for y in range(99):
      #implement a min reward threshold.

      if self.qTable[self.curState].max() < self.minReward or self.curState+1 == 100:
        break

      eCompare = random.random()
      
      if eCompare < epi: # random action
        choices = self.movement(True)


        if self.x == self.size-1 and self.y == self.size-1:
          self.qTable[self.curState][choices] = self.qTable[self.curState][choices] + .1*(self.reward()["complete"] + .99*self.qTable[self.curState+1].max() - self.qTable[self.curState][choices])
          #print("yaa1")
          break
        elif choices == "error":
          #print("moooo")
          break
          


      else: # exploitive action
        choices = self.movement(False)

        if self.x == self.size-1 and self.y == self.size-1:
          self.qTable[self.curState][choices] = self.qTable[self.curState][choices] + .1*(self.reward()["complete"] + .99*self.qTable[self.curState+1].max() - self.qTable[self.curState][choices])
          print("Success")
          break
        elif choices == "error":
          #print("moooo")
          break

      #print(self.x,self.y,self.size)
      self.preC += [(self.x,self.y)]
      self.curState += 1



mazer = MazeSolver(masterArr2)

print(mazer.mainRun())