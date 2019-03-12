import random
import mc
import GridWorld

debug = True

class Agent:

    def __init__(self, gridWorld, policy):
        #1 = North, 2 = East, 3 = South, 4 = West
        self.playerX = gridWorld.startPoint['x']
        self.playerY = gridWorld.startPoint['y']
        self.currentGrid = gridWorld.startPoint['grid']
        self.reward = 0
        self.policy = mc.monteCarlo(gridWorld.stateGrid(), gridWorld.stateGrid())
        self.North = 1
        self.East = 2
        self.South = 3
        self.West = 4
        self.Done = False
        self.moveCount = 0
        self.stateActionArray = []

    def move(self):
        state = {'grid' : self.currentGrid, 'x' : self.playerX, 'y' : self.playerY}
        self.moveCount += 1 
        move = self.policy.onPolicyEsoft(state)
        state['action'] = move
        self.policy.StateActionTimesVisted[move-1].arrayOfGrids[state['grid']-1].grid[state['x']][state['y']] += 1
        self.stateActionArray.append(state)
        print("State: {}, stateActionArray: {}".format(state, self.stateActionArray)) if debug else False
        return move

    def update(self,reward):
        self.reward += reward
        self.stateActionArray[len(self.stateActionArray)-1]['reward'] = reward
        print("Reward: stateActionArray: {}".format(self.stateActionArray)) if debug else False

        

    def playerStatus(self):
        return "agent Status: Reward: {},  X: {}, Y: {}, Gird: {}, MoveCount: {}".format(self.reward, self.playerX,self.playerY,self.currentGrid, self.moveCount)
    
    def resetAgent(self,X,Y,Grid):
        self.Done = False
        self.playerX = X
        self.playerY = Y
        self.currentGrid = Grid
        self.moveCount = 0
        self.stateActionArray = []