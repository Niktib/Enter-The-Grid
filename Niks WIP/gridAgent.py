import random
import mc
class Agent:

    def __init__(self, X, Y, grid, policy):
        #1 = North, 2 = East, 3 = South, 4 = West
        self.playerX = X
        self.playerY = Y
        self.currentGrid = grid
        self.reward = 0
		self.numOfActions = 4
        self.policy = mc.monteCarlo(self.numOfActions)
		
        self.North = 1
        self.East = 2
        self.South = 3
        self.West = 4

    def move(self):
        state = {'grid' : self.currentGrid, 'x' : self.playerX, 'y' : self.playerY}
        return self.policy.decision(state)

    def playerStatus(self):
        return "agent Status: Reward: {},  X: {}, Y: {}, Grid: {}".format(self.reward, self.playerX,self.playerY,self.currentGrid)
		
	def playerStateSetUp(self, gridDimensions):
	#Recieves GridDimensions from GridWorld
		stateMap = []			
		for i in range(gridDimensions):
			#X dimensions of the grids
			individualGrid = [None] * gridDimensions[0]
			for j in range(gridDimensions[0]):
				#Y dimensions of the grid
				individualGrid[j] = [None] * gridDimensions[1]
				for k in range(gridDimensions[1]):
					#All possible Actions
					individualGrid[j][k] = [0] * self.numOfActions
			#Add it to the total stateMap
			stateMap.add(individualGrid)
		self.policy.setUpState(stateMap)