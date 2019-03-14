import GridWorld
import gridAgent
import random
import mc
import q
import sarsa
import os
import time as time

debug = False
class testbed:

	#Also all those greek letters
	
	def __init__(self, mcLearning = False, sarsaLearning = False, qLearning = False, randomSpwan=False, p1=0.8, p2=0.1, epsilon = 0.1, gamma = 0.9, alpha = 0.1):
		self.gridWorld = GridWorld.GridWorld({"grid": 3, "x" : 4 , "y" : 0})
		self.gridWorld.pieceItTogether()
		
		self.mcLearning = mcLearning
		self.sarsaLearning = sarsaLearning
		self.qLearning = qLearning
		#Epsilon, Gamma, Alpha
		if self.mcLearning: self.policy = mc.monteCarlo(epsilon, gamma, alpha)
		if self.sarsaLearning: self.policy = sarsa.sarsaLearning(epsilon, gamma, alpha)
		if self.qLearning: self.policy = q.qlearning(epsilon, gamma, alpha)
		
		
	def run(self, iterations, episodes, steps, printInfo = False):
		totalSuccess = 0
		
		agentArray= []
		for i in range(episodes - len(agentArray) +1): agentArray.append([random.randint(0,4),random.randint(0,4),random.randint(0,len(self.gridWorld.arrayOfGrids)-1)+1])
		
		for iter in range(1, iterations+1):
			
			iterationStart = time.time()
			writeUp = ""
			agent = gridAgent.Agent(2,3,3,self.policy)
			agent.playerStateSetUp(self.gridWorld.understandingState())
			for ep in range(1,episodes+1):
				episodeStart = time.time()
				episodeAverageTime = 0
				while True:
					if printInfo:
						print("Iter: {}, Ep: {}, {}".format(iter, ep, agent.playerStatus()))
						self.gridWorld.printOut(agent.agentState(), True)
					agent.results(self.gridWorld.agentMove(agent.agentState(), agent.move()))
					if self.sarsaLearning or self.qLearning: agent.sarsaUpdate()
					print("Iter: {}, Ep: {}, {}".format(iter, ep, agent.playerStatus())) if debug else False#debug
					#Check if goal state has been reached?
					if self.gridWorld.finished: totalSuccess += 1
					if self.gridWorld.finished or agent.moves> steps:
						#Reset goal state
						self.gridWorld.finished = False
						break
				#At end of episode, update policy and grab it from agent to give to new agent
				episodeEnd = time.time()
				episodeAverageTime = episodeAverageTime + 1/ep * ( (episodeEnd - episodeStart) - episodeAverageTime)
				if self.mcLearning: agent.mcUpdate()
				
				self.policy = agent.policyRetrieval()
				writeUp += "Episode {} ".format(ep) + agent.agentInformation() + " Time Taken: {} \n".format(episodeEnd - episodeStart)
				#agent = gridAgent.Agent(1,2,3,self.policy)
				agent = gridAgent.Agent(agentArray[ep][0],agentArray[ep][1],agentArray[ep][2] ,self.policy)
			iterationEnd = time.time()
			
		print("Last Iterations Time is: {} \nAverage Episode time is: {} with a total # of successful runs: {}".format(iterationEnd - iterationStart, episodeAverageTime, totalSuccess))
		self.policy.printOut()
		f = open(os.path.dirname(os.path.realpath(__file__)) + "\Algorithm {} Epsilon={} Alpha={} Gamma={}.txt".format(self.policy.name, self.policy.epsilon, self.policy.alpha, self.policy.gamma),"w")
		f.write(writeUp)
		f.close()
