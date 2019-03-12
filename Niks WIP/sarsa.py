class sarsa:
     
     def __init__(self):
         pass
		
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
		
	def updateStates(self, statesTraversed, newState):
		#statesTraversed is an array in format [[grid, x, y], action]
		#New state in similar format, but no reward
		s = statesTraversed[0] #State
		a = statesTraversed[1] #Chosen Action
		r = statesTraversed[2] #Reward
		sPrime = newState[0] #New State
		aPrime = newState[1] #New Action
		returnValue = r + self.gamma * self.stateActionMap[sPrime[0]][sPrime[1]][sPrime[2]][aPrime][0]
		currentValue = self.stateActionMap[s[0]][s[1]][s[2]][a][0]
		#Qn = Qn + aplha * (Rt + Qn)
		self.stateActionMap[s[0]][s[1]][s[2]][a][0] = currentValue + self.alpha * (returnValue - currentValue) #need the update function for action picking