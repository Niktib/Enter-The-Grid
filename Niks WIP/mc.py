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
		if random.random() < self.epsilon:
			return self.explore()
		else:
			return self.exploit(state)
	
	def exploit(self, state):
		#contains the values each action has been granted
		actionArray = []
		numberOfTimesVisited = []
		print("State: {}".format(state))
		print("Dimensions: {} by {}".format(len(self.stateActionMap[state[0]-1]),len(self.stateActionMap[state[0]-1][state[1]]) ))
		arrayOfActions = self.stateActionMap[state[0]-1][state[1]][state[2]]
		for i in range(len(arrayOfActions)):
			actionArray.append(arrayOfActions[i][0])
			numberOfTimesVisited.append(arrayOfActions[i][1])
		#First time visit always explore
		if max(numberOfTimesVisited) == 0: return self.explore()
		#each index is representative of the action,so 1 = North, 2 = east, etc. 
		#By finding the max and its index we know the greedy action.
		action = actionArray.index(max(actionArray))
		if action < 0: action = 0
		return action
        
	def explore(self):
		#No need to figure out which action in the state, we just need a random action
		return random.randint(1,self.numOfActions)
		
	def updateStates(self, statesTraversed):
		#statesTraversed is an array in format [grid, x, y, action]
		statesTraversed.reverse()
		totalReturn = 0
		for i in range(len(statesTraversed)):
			s = statesTraversed[i][0] #State
			a = statesTraversed[i][1]-1 #Chosen Action
			r = statesTraversed[i][2] #Reward
			totalReturn += r + self.gamma * totalReturn 
			
			print("State: {}, Action: {}".format(s,a))
			currentValue = self.stateActionMap[s[0]-1][s[1]][s[2]][a][0]
			self.stateActionMap[s[0]-1][s[1]][s[2]][a][1] += 1
			numberOfTimesPicked = self.stateActionMap[s[0]-1][s[1]][s[2]][a][1]
			#Qn = Qn + 1/n (Rt - Qn)
			self.stateActionMap[s[0]-1][s[1]][s[2]][a][0] = currentValue + 1/numberOfTimesPicked * (totalReturn - currentValue) #need the update function for action picking
			