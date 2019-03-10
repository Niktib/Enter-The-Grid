import random

class Agent:

    def __init__(self, X, Y, grid, policy):
        #1 = North, 2 = East, 3 = South, 4 = West
        self.playerX = X
        self.playerY = Y
        self.currentGrid = grid
        self.reward = 0
        self.policy = policy
        self.North = 1
        self.East = 2
        self.South = 3
        self.West = 4

    def move(self):
        return self.West

    def playerStatus(self):
        return "agent Status: Reward: {},  X: {}, Y: {}, Gird: {}".format(self.reward, self.playerX,self.playerY,self.currentGrid)