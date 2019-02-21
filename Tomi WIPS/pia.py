import random
from datetime import datetime
import random
class PolicyIteration:
	def __init__(self, p1=0.8, p2=0.1, rUp=-1, rDown=-1, rRight=-1, rLeft=-1, x=4,  y=4, discount=0.95, accuracy=0.001):
		self.rUp = rUp
		self.rDown = rDown
		self.rLeft = rLeft
		self.rRight = rRight
		self.Discount = discount
		self.theta = accuracy
		self.p1 = p1
		self.p2 = p2
		
		self.upProb = 0.25
		self.upProb = 0.25
		self.upProb = 0.25
		self.upProb = 0.25

		self.x = x
		self.y = y
		self.value = [0] * self.x
		for i in range(self.x):
			self.value[i] = [0] * self.y
			
		self.setTerminal()
			
	def setTerminal(self):
		#places terminal messages in grid locations assigned
		self.value[0][0] = "T"
		self.value[self.x-1] [self.y-1] = "T"
					
	def iteration(self, iterate):
		delta = 0
		areWeDoneHere = False
		for runTime in range(iterate):
			for i in range(self.x):
				for j in range(self.y):
					if type(self.value[i][j]) is not str :
						oldValue = 0
						oldValue = self.value[i][j]
						self.value[i][j] = self.bellmanBackup(i, j)
						if self.theta > (abs(oldValue-self.value[i][j])): areWeDoneHere = True
			if areWeDoneHere: break
			print("For Iteration {}:\n".format(runTime+1))
			self.printOut()
		
		print("Final Iteration {}:\n".format(runTime+1))
		self.printOut()
				
	def printOut(self):
		for i in self.value: print(i)
		print("\n")


	def policyChoice(self):
		result = random.random()
		adjacent = (1 - (self.p1 + self.p2)) / 2
		if direction == 1: 
			#Up
			reward = self.rUp
		elif direction == 2: 
			#Down
			reward = self.rDown
		elif direction == 3: 
			#Left
			reward = self.rLeft
		elif direction == 4: 
			#Right
			reward = self.rRight
    

	def bellmanBackup(self, i, j, direction):
	#j is x-axis, so left is -1 and right is +1
	#i is y-axis, so up is -1 and down is +1
		reward = 0
		if direction == 1: 
			#Up
			reward = self.rUp
			arr = [-1, 0, -1, 1, -1, -1]
		elif direction == 2: 
			#Down
			reward = self.rDown
			arr = [1, 0, 1, -1, 1, 1]
		elif direction == 3: 
			#Left
			reward = self.rLeft
			arr = [0, -1, -1, -1, 1, -1]
		elif direction == 4: 
			#Right
			reward = self.rRight
			arr = [0, 1, 1, 1, -1, 1]
			
		adjacent = (1 - (self.p1 + self.p2)) / 2 
		#Going Up
		action = (self.p1 *(reward + self.Discount * self.errorCheck(i + arr[0], j + arr[1]))) + (self.p2 *(reward + self.Discount * self.errorCheck(i, j))) + (adjacent *(self.rUp + self.Discount * self.errorCheck(i + arr[2], j + arr[3]))) + (adjacent *(self.rUp + self.Discount * self.errorCheck(i + arr[4], j + arr[5])))
		
		return action
	
	def errorCheck(self, i, j):
		if i < 0: i = 0
		elif i > self.x - 1: i = self.x - 1
		if j < 0: j = 0
		elif j > self.y - 1: j = self.y - 1
		
		if type(self.value[i][j]) is str : return 0
		return self.value[i][j]
	
test = PolicyIteration(0.1,0.5,-1,-1,-1,-1,5,4)
test.printOut()
test.iteration(100)