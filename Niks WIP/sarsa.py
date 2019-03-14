# Name, Student Number
# Oluwatomilayo Adegbite, 500569283
# Nikolas Maier, 500461990
import random
import gridworldtestbed as GTB

class sarsaLearning:
     
	def __init__(self, epsilon = 0.1, gamma = 0.9, alpha = 0.1):
		self.epsilon = epsilon
		self.gamma = gamma
		self.alpha = alpha
		self.name = "SARSA"
		
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
		numberOfTimesVisited = 0
		arrayOfActions = self.stateActionMap[state[0]-1][state[1]][state[2]]
		for i in range(len(arrayOfActions)):
			numberOfTimesVisited += arrayOfActions[i]
		#First time visit always explore
		if numberOfTimesVisited == 0: return self.explore()
		#each index is representative of the action,so 1 = North, 2 = east, etc. 
		#By finding the max and its index we know the greedy action.
		action = arrayOfActions.index(max(arrayOfActions)) + 1
		if action <= 0: action = 1
		return action
        
	def explore(self):
		#No need to figure out which action in the state, we just need a random action
		return random.randint(1,self.numOfActions)
		
	def updateStates(self, statesTraversed, newState):
		#statesTraversed is an array in format [[grid, x, y], action]
		#New state in similar format, but no reward
		s = statesTraversed[0][0] #State
		a = statesTraversed[0][1]-1 #Chosen Action
		r = statesTraversed[0][2] #Reward
		sPrime = newState #New State
		aPrime = self.decision([sPrime[2],sPrime[1],sPrime[0]])-1 #New Action
		returnValue = r + self.gamma * self.stateActionMap[sPrime[2]-1][sPrime[1]][sPrime[0]][aPrime]
		
		currentValue = self.stateActionMap[s[0]-1][s[1]][s[2]][a]
		#Qn = Qn + alpha * (Rt + Qn)
		self.stateActionMap[s[0]-1][s[1]][s[2]][a] = currentValue + self.alpha * (returnValue - currentValue)
		
	def printOut(self):
		for i in range(len(self.stateActionMap)):
			#print("Grid #{}:".format(i+1))
			for x in range(len(self.stateActionMap[i])):
				for y in range(len(self.stateActionMap[i][x])):
					self.stateMap[i][x][y] = self.policyPrint(self.stateActionMap[i][x][y])
		
		for i in range(len(self.stateMap)):
			print("Grid #{}:".format(i+1))
			self.printGrid(self.stateMap[i])
		
	def policyPrint(self, arrayOfActions):
		action = arrayOfActions.index(max(arrayOfActions))
		if sum(arrayOfActions) == 0:
			return 'N'
		elif action == 0:
			return '^'
		elif action == 1:
			return '>'
		elif action == 2:
			return 'v'
		elif action == 3:
			return '<'
		else:
			return '0'
	def printGrid(self, gridArray):
		pStr = "\t"
		x = len(gridArray)
		y = len(gridArray[0])
		
		for i in range(x):
			pStr = pStr + "____" 
		pStr = pStr + "_\n"
		for i in range(x):
				pStr = pStr + "\t"
				for j in range(y):
					pStr = pStr + "|   "
				pStr = pStr + "|\n\t"
				for j in range(y):
					pStr = pStr + "| " + str(gridArray[i][j]) + " "
				pStr = pStr + "|\n\t"
				for j in range(y):
					pStr = pStr + "|___"
				pStr = pStr + "|\n"
		print(pStr)
		
		
print("The default settings are: \n\tp1 = 0.8\n\tp2 = 0.1")
p1 = 0.8
p2 = 0.1
choice = input("Do you want to change these defaults? Y/N\n")
if choice == "Y" or choice =="y":
	p1 = double(input("p1 = "))
	p2 = double(input("p2 = "))
choice = input("The defaults for \n\tgamma = 0.9\n\talpha = 0.1\n\tepsilon = 0.1 \ndo you want to change them?\n Y/N\n")
gamma = 0.9
alpha = 0.1
epsilon = 0.1
if choice == "Y" or choice =="y":
	gamma = double(input("gamma = "))
	alpha = double(input("alpha = "))
	epsilon = double(input("epsilon = "))
print("Number of Iterations is set to 1 and episodes equals 200 with maxiumum steps per episode set to 1000")
iterations = 1
episodes = 200
steps = 1000
choice = input("Do you want to change these? Y/N\n")
if choice == "Y" or choice =="y":
	iterations = input("Iterations: ")
	episodes = input("Episodes: ")
	steps = input("Maximum steps: ")
	
test = GTB.testbed(False,True,False,p1, p2, epsilon, gamma, alpha)
test.run(iterations, episodes, steps)
input("Press Enter key to exit")	
		