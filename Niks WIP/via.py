import time as time

class ValueIteration:
	def __init__(self, p1=0.8, p2=0.1, rUp=-1, rDown=-1, rRight=-1, rLeft=-1, x=4,  y=4, discount=0.95, accuracy=0.001):
		self.rUp = rUp
		self.rDown = rDown
		self.rLeft = rLeft
		self.rRight = rRight
		self.Discount = discount
		self.theta = accuracy
		self.p1 = p1
		self.p2 = p2
		self.actions = [0,1,2,3]
		
		self.x = x
		self.y = y
		self.value = [0] * self.x
		self.policy = [0] * self.x
		for i in range(self.x):
			self.value[i] = [0] * self.y
			self.policy[i] = [0] * self.y
			
		self.setTerminal()
			
	def setTerminal(self):
		#places terminal messages in grid locations assigned
		self.value[0][0] = "T"
		self.value[self.x-1] [self.y-1] = "T"
					
	def iteration(self, iterate, printResults=False):
		delta = 0
		areWeDoneHere = False
		for runTime in range(iterate):
			start = time.time()
			for i in range(self.x):
				for j in range(self.y):
					if type(self.value[i][j]) is not str :
						oldValue = 0
						oldValue = self.value[i][j]
						results = self.bellmanBackup(i, j)
						self.value[i][j] = results[0]
						self.policy[i][j] = results[1]
						if self.theta > max([delta, abs(oldValue-self.value[i][j])]): areWeDoneHere = True
					else: 
						self.policy[i][j] = "T"
			end = time.time()
			print("Iteration: {} has taken {}\n".format(runTime+1, end-start))
			if printResults:
				self.printOut()
			if areWeDoneHere: break
		self.printOutPolicy()
		
	def printOut(self):
		for i in self.value: print(i)
		print("\n")

	def bellmanBackup(self, i, j):
	#j is x-axis, so left is -1 and right is +1
	#i is y-axis, so up is -1 and down is +1
		adjacent = (1 - (self.p1 + self.p2)) / 2 
		#Going Up
		action1 = (self.p1 *(self.rUp + self.Discount * self.errorCheck(i-1, j))) + (self.p2 *(self.rUp + self.Discount * self.errorCheck(i, j))) + (adjacent *(self.rUp + self.Discount * self.errorCheck(i-1, j+1))) + (adjacent *(self.rUp + self.Discount * self.errorCheck(i-1, j-1)))
		#Going down
		action2 = (self.p1 *(self.rDown + self.Discount * self.errorCheck(i+1, j))) + (self.p2 *(self.rDown + self.Discount * self.errorCheck(i, j))) + (adjacent *(self.rDown + self.Discount * self.errorCheck(i+1, j+1))) + (adjacent *(self.rDown + self.Discount * self.errorCheck(i+1, j-1)))
		#Going left
		action3 = (self.p1 *(self.rLeft + self.Discount * self.errorCheck(i, j-1))) + (self.p2 *(self.rLeft + self.Discount * self.errorCheck(i, j))) + (adjacent *(self.rLeft + self.Discount * self.errorCheck(i-1, j-1))) + (adjacent *(self.rLeft + self.Discount * self.errorCheck(i+1, j-1)))
		#Going right
		action4 = (self.p1 *(self.rRight + self.Discount * self.errorCheck(i, j+1))) + (self.p2 *(self.rRight + self.Discount * self.errorCheck(i, j))) + (adjacent *(self.rRight + self.Discount * self.errorCheck(i-1, j+1))) + (adjacent *(self.rRight + self.Discount * self.errorCheck(i+1, j+1)))
		
		arrayOfActions = [action1, action2, action3, action4]
		
		return [max(arrayOfActions), arrayOfActions.index(max(arrayOfActions))]
	
	def errorCheck(self, i, j):
		if i < 0: i = 0
		elif i > self.x - 1: i = self.x - 1
		if j < 0: j = 0
		elif j > self.y - 1: j = self.y - 1
		
		if type(self.value[i][j]) is str : return 0
		return self.value[i][j]
	
	def printOutPolicy(self):
		self.policy 
		pStr = "\t"
		for i in range(self.x): pStr = pStr + "____" 
		pStr = pStr + "_\n"
		for i in range(self.x):
			
			pStr = pStr + "\t"
			for j in range(self.y):
				pStr = pStr + "|   "
			pStr = pStr + "|\n\t"
			for j in range(self.y):
				printingValue = self.printPretty(self.policy[i][j])
				pStr = pStr + "| " + printingValue + " "
			pStr = pStr + "|\n\t"
			for j in range(self.y):
				pStr = pStr + "|___"
			pStr = pStr + "|\n"
		print(pStr)
	
	def printPretty(self, recPolicy):
		if recPolicy == 0:
			return "^"
		elif recPolicy == 1:
			return "v"
		elif recPolicy == 2:
			return "<"
		elif recPolicy == 3:
			return ">"
		elif recPolicy == "T":
			return "0"