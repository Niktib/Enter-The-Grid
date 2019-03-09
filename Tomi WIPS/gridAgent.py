import random

class Agent:

    def __init__(self, X, Y, grid, policy):
        self.playerX = X
        self.playerY = Y
        self.currentGrid = grid
        self.reward = 0
        self.policy = policy

    def move(self):
        return 1

    def playerStatus(self):
        return "agent Status: Reward: {},  X: {}, Y: {}, Gird: {}".format(self.reward, self.playerX,self.playerY,self.currentGrid)