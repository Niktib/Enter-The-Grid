import random

class monteCarlo:
     
    def __init__(self, epsilon = 0.1, gamma = 0.9):
		self.epsilon = epsilon
		self.gamma = gamma
		
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
	
	def exploit(self, state):
		#contains the values each action has been granted
		actionArray = []
		numberOfTimesVisited = []
		arrayOfActions = self.stateActionMap[state[0]][state[1]][state[2]]
		for i in range(arrayOfActions):
			actionArray.append(arrayOfActions[0])
			numberOfTimesVisited.append(arrayOfActions[1])
		#First time visit always explore
		if max(numberOfTimesVisited) == 0: return self.explore()
		#each index is representative of the action,so 1 = North, 2 = east, etc. 
		#By finding the max and its index we know the greedy action.
		return arrayOfActions.index(max(actionArray))
        
	def explore(self):
		#No need to figure out which action in the state, we just need a random action
		return random.randint(1,self.numOfActions)
		
	def updateStates(self, statesTraversed):
		#statesTraversed is an array in format [grid, x, y, action]
		statesTraversed.reverse()
		totalReturn = 0
		for i in range(statesTraversed)
			s = statesTraversed[i][0] #State
			a = statesTraversed[i][1] #Chosen Action
			r = statesTraversed[i][2] #Reward
			totalReturn += r + self.gamma * totalReturn 
			currentValue = self.stateActionMap[s[0]][s[1]][s[2]][a][0]
			numberOfTimesPicked = self.stateActionMap[s[0]][s[1]][s[2]][a][1]
			#Qn = Qn + 1/n (Rt + Qn)
			self.stateActionMap[s[0]][s[1]][s[2]][a][0] = currentValue + 1/numberOfTimesPicked * (totalReturn - currentValue) #need the update function for action picking
			