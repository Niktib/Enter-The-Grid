import random

class monteCarlo:
     
    def __init__(self, epsilon = 0.1):
		self.epsilon = epsilon
		
	def numberOfActions(self, numOfActions=4):
		self.numOfActions = numOfActions
		
	def setUpState(self, blankStateActionArray, blankStateArray):
		self.stateMap = blankStateArray
		self.stateActionMap = blankStateActionArray
		
	def decision(self, state):
		if random.random() < epsilon:
			return self.explore(state)
		else:
			return self.exploit(state)
	
	
	def explore(self, state):
		#contains the values each action has been granted
		arrayOfActions = self.stateActionMap[state[0]][state[1]][state[2]]
		#each index is representative of the action,so 1 = North, 2 = east, etc. 
		#By finding the max and its index we know the greedy action.
		return arrayOfActions.index(max(arrayOfActions))
        
	def explore(self):
		#No need to figure out which action in the state, we just need a random action
		return random.randint(1,self.numOfActions)
		
	def updateStates(self, statesTraversed, returnValue):
		#statesTraversed is an array in format [grid, x, y, action]
		for i in range(statesTraversed)
			s = statesTraversed[i]
			self.stateMap[s[0]][s[1]][s[2]] = 0 #need the update function for state
			self.stateActionMap[s[0]][s[1]][s[2]][s[3]] = 0 #need the update function for action picking
			