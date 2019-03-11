import random

class monteCarlo:
     
    def __init__(self, numOfActions=4, epsilon = 0.1):
		self.epsilon = epsilon
        self.numOfActions = numOfActions
		 
	def setUpState(self, blankStateArray):
		self.stateMap = blankStateArray
	
	def decision(self, state):
		if random.random() < epsilon:
			return self.explore(state)
		else:
			return self.exploit(state)
	
	
	def explore(self, state):
		#contains the values each action has been granted
		arrayOfActions = self.stateMap[state[0]][state[1]][state[2]]
		#each index is representative of the action,so 1 = North, 2 = east, etc. 
		#By finding the max and its index we know the greedy action.
		return arrayOfActions.index(max(arrayOfActions))
        
	def explore(self):
		#No need to figure out which action in the state, we just need a random action
		return random.randint(1,self.numOfActions)
        