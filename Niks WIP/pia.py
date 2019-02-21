# Name, Student Number
# Oluwatomilayo Adegbite, 500569283
# Nikolas Maier, 500461990

import random
from datetime import datetime
import time as time

class PolicyIteration:
	def __init__(self, p1=0.8, p2=0.1, rUp=-1, rDown=-1, rRight=-1, rLeft=-1, x=4,  y=4, discount=0.95, accuracy=0.001):
		#Initializes all the reoccuring values that are relevant to the test
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
		#Creates the array to store all the states and all the Policy
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
	

	def policyIterating(self, numOfIterationsMax, printResults=False):
		x = 0
		#Intial policy setUp for each state
		for i in range(self.x):
			for j in range(self.y):
				if type(self.value[i][j]) is not str :
					self.policy[i][j] = self.randomMove()
				else:
					self.policy[i][j] = "T"
		
		#The loop of Policy Iteration
		while True:
			x+=1
			start = time.time()
			self.policyEvaluation(numOfIterationsMax, printResults)
			if self.policyImprovement(): break
			end = time.time()
			print("Iteration: {} has taken {}".format(x, end-start))
		self.printOutPolicy()
		
	def policyEvaluation(self, iterate, printResults = False):
		#Policy evaluation loop
		#Takes the current policy action and does the math to check if we need to keep looping.
		delta = 0
		areWeDoneHere = False
		for runTime in range(iterate):
			for i in range(self.x):
				for j in range(self.y):
					if type(self.value[i][j]) is not str :
						oldValue = 0
						oldValue = self.value[i][j]
						self.value[i][j] = self.bellmanBackup(i, j, self.policy[i][j])
						if self.theta > max([delta, abs(oldValue-self.value[i][j])]):
							areWeDoneHere = True
					else:
						self.policy[i][j] = "T"
			if printResults:
				print("For Iteration {}:\n".format(runTime+1))
				self.printOut()
			if areWeDoneHere: break
		
	def printOut(self):
		#prints out the Value array in a rough grid formation
		for i in self.value: print(i)
		print("\n")
		
		
	def policyImprovement(self):
		#Basic policy improvement loop that checks if there exists an action that is better than the current Policy action
		policyStable = True
		for i in range(self.x):
			for j in range(self.y):
				if type(self.value[i][j]) is not str :
					action = self.policy[i][j]
					self.policy[i][j] = self.policyImpMath(i,j)
					if action != self.policy[i][j]: policyStable = False
		return policyStable

		
	def policyImpMath(self, i, j):
	#Checks all actions from current state to see if there is a better option at the moment
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
		
		return arrayOfActions.index(max(arrayOfActions))
	def bellmanBackup(self, i, j, direction):
	#j is x-axis, so left is -1 and right is +1
	#i is y-axis, so up is -1 and down is +1
	#Below we have an array assigned the changes of values based on each option of where a move can end up
		reward = 0
		if direction == 0: 
			#Up
			reward = self.rUp
			arr = [-1, 0, -1, 1, -1, -1]
		elif direction == 1: 
			#Down
			reward = self.rDown
			arr = [1, 0, 1, -1, 1, 1]
		elif direction == 2: 
			#Left
			reward = self.rLeft
			arr = [0, -1, -1, -1, 1, -1]
		elif direction == 3: 
			#Right
			reward = self.rRight
			arr = [0, 1, 1, 1, -1, 1]
			
		adjacent = (1 - (self.p1 + self.p2)) / 2 
		#One stupid big math equation of each possible Probability * ( Action, Reward and S') combination
		action = (self.p1 *(reward + self.Discount * self.errorCheck(i + arr[0], j + arr[1]))) + (self.p2 *(reward + self.Discount * self.errorCheck(i, j))) + (adjacent *(self.rUp + self.Discount * self.errorCheck(i + arr[2], j + arr[3]))) + (adjacent *(self.rUp + self.Discount * self.errorCheck(i + arr[4], j + arr[5])))
		
		return action
	
	def errorCheck(self, i, j):
		#ErrorCheck makes sure that if the S' state is outside of the grid it gets pushed back into an actual state.
		if i < 0: i = 0
		elif i > self.x - 1: i = self.x - 1
		if j < 0: j = 0
		elif j > self.y - 1: j = self.y - 1
		
		if type(self.value[i][j]) is str : return 0
		return self.value[i][j]
		
	def randomMove(self):
		#Exactly what it says on the tin, for the first assigning of policy action we need to pick it randomly. That is what this does
		move = random.random()
		if move < 0.25:
			return self.actions[0]
		elif move < 0.50:
			return self.actions[1]
		elif move < 0.75:
			return self.actions[2]
		else:
			return self.actions[3]
			
	def printOutPolicy(self):
	#Outputs a pretty grid where each grid center is replaced with the policy for that state
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
	#Replaces the numeric actions in policy with arrows to make the grid more legible
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
		