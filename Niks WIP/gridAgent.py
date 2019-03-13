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
		state = [self.currentGrid, self.playerX, self.playerY]
		action = self.policy.decision(state)
		self.stateActionArray.append([state, action])
		return action

	def results(self, resultsArray):
		self.playerX = resultsArray[0]
		self.playerY = resultsArray[1]
		self.currentGrid = resultsArray[2]
		self.stateReward(resultsArray[3])
		self.reward += resultsArray[3]

	def stateReward(self, rewardRecd):
		self.stateActionArray[-1].append(rewardRecd)

	def agentState(self):
		return [self.playerX, self.playerY, self.currentGrid]

	def playerStatus(self):
		return "agent Status: Reward: {},  X: {}, Y: {}, Grid: {}".format(self.reward, self.playerX,self.playerY,self.currentGrid)
		
	def sarsaUpdate(self):
		self.policy.updateStates(self.stateActionArray, self.agentState())
		self.stateActionArray = []
		
	def mcUpdate(self):
		self.policy.updateStates(self.stateActionArray)
	
	def policyRetrieval(self):
		return self.policy

	def playerStateSetUp(self, gridDimensions):
	#Recieves GridDimensions from GridWorld
		stateMap = []
		stateActionMap = []
		for i in range(len(gridDimensions)):
			#X dimensions of the grids
			individualGrid = [None] * gridDimensions[i][0]
			individualActionGrid = [None] * gridDimensions[i][0]
			for j in range(gridDimensions[i][0]):
				#Y dimensions of the grid
				individualGrid[j] = [0] * gridDimensions[i][1]
				individualActionGrid[j] = [None] * gridDimensions[i][1]
				for k in range(gridDimensions[i][1]):
					#All possible Actions
					individualActionGrid[j][k] = [0] * self.numOfActions
			#Add it to the total stateMap
			stateActionMap.append(individualActionGrid)
			stateMap.append(individualGrid)
			
		self.policy.setUpState(stateActionMap, stateMap)