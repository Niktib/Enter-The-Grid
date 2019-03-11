import random
import mc
import q
import sarsa
class Agent:

    def __init__(self, X, Y, grid, policy):
        #1 = North, 2 = East, 3 = South, 4 = West
        self.playerX = X
        self.playerY = Y
        self.currentGrid = grid
        self.reward = 0
		self.numOfActions = 4
		
		self.stateActionArray = []
        self.policy = policy
		self.policy.numberOfActions(self.numOfActions)

    def move(self):
        state = {'grid' : self.currentGrid, 'x' : self.playerX, 'y' : self.playerY}
		action = self.policy.decision(state)
		self.stateActionArray.add([state, action])
        return action
	
	def results(self, resultsArray):
		self.playerX = resultsArray[0]
		self.playerY = resultsArray[1]
		stateReward(resultsArray[2])
		self.reward += resultsArray[2]
	
	def stateReward(self, rewardRecd):
		self.stateActionArray[-1].add(rewardRecd)
	
	def agentState(self):
		return [self.playerX, self.playerY, self.currentGrid]
	
    def playerStatus(self):
        return "agent Status: Reward: {},  X: {}, Y: {}, Grid: {}".format(self.reward, self.playerX,self.playerY,self.currentGrid)
		
	def playerStateSetUp(self, gridDimensions):
	#Recieves GridDimensions from GridWorld
		stateMap = []
		stateActionMap = []
		for i in range(gridDimensions):
			#X dimensions of the grids
			individualGrid = [None] * gridDimensions[0]
			individualActionGrid = [None] * gridDimensions[0]
			for j in range(gridDimensions[0]):
				#Y dimensions of the grid
				individualGrid[j] = [0] * gridDimensions[1]
				individualActionGrid[j] = [None] * gridDimensions[1]
				for k in range(gridDimensions[1]):
					#All possible Actions
					individualActionGrid[j][k] = [0] * self.numOfActions
			#Add it to the total stateMap
			stateActionMap.add(individualActionGrid)
			stateMap.add(individualGrid)
		self.policy.setUpState(stateMap, stateActionMap)