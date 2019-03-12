import random
import GridWorld
import copy

debug = True
class monteCarlo:
     
     def __init__(self, valueState, policyState,epislon=0.1, gamma=0.9, numOfActions=4):
          self.gamma = gamma
          self.epislon = epislon
          self.StateAction = list()
          self.StateActionTimesVisted = list()
          for i in range(4):
               #0 = North, 1 = East, 2 = South, 3 = West
               self.StateAction.append(copy.deepcopy(valueState))
               self.StateActionTimesVisted.append(copy.deepcopy(valueState))
          self.policy = policyState
          self.initPolicy()
          self.printPolicyValue()
          

     def decision(self,state):
          move = self.policy.arrayOfGrids[state['grid']-1].grid[state['x']][state['y']]
          print("Decision: {}".format(move))
          return move
     
     def exlpore(self):
          return random.randint(1,4)

     def exploit(self,state):
          move = self.policy.arrayOfGrids[state['grid']-1].grid[state['x']][state['y']]
          print("Decision: {}".format(move))
          return move

     def onPolicyEsoft(self, state):
          ran = random.random()
          print("E-sort: E: {}, ran: {}".format(self.epislon,ran)) if debug else False
          if ran < self.epislon:
               return self.exlpore()
          else:
               return self.exploit(state)
          pass

     def initPolicy(self):
          for grid in self.policy.arrayOfGrids:
               #initalize random policy
               for i in range(len(grid.grid)):
                    for j in range(len(grid.grid[i])):
                        grid.grid[i][j] = random.randint(1,4)

     def updateStates(self, statesTraversed):
          #statesTraversed is an array in format [grid, x, y, action]
          statesTraversed.reverse()
          totalReturn = 0
          for step in statesTraversed:
               totalReturn += step['reward'] + self.gamma * totalReturn 
               currentValue = self.StateAction[step['action'] - 1].arrayOfGrids[step['grid']-1].grid[step['x']][step['y']]
               numberOfTimesPicked = self.StateActionTimesVisted[step['action'] - 1].arrayOfGrids[step['grid']-1].grid[step['x']][step['y']]
               #self.stateMap[s[0]][s[1]][s[2]] = 0 #need the update function for state
               #Qn = Qn + 1/n (Rt + Qn)
               self.StateAction[step['action']-1].arrayOfGrids[step['grid']-1].grid[step['x']][step['y']] = currentValue + (1/numberOfTimesPicked) * (totalReturn - currentValue) #need the update function for action picking
               bestAction = step['action']
               bestActionValue = self.StateAction[step['action']-1].arrayOfGrids[step['grid']-1].grid[step['x']][step['y']]
               for action in range(len(self.StateAction)):
                    if bestActionValue <  self.StateAction[action].arrayOfGrids[step['grid']-1].grid[step['x']][step['y']]:
                         bestAction = action+1 #because index starts at 0 and action numbered 1-4
                         bestActionValue = self.StateAction[action].arrayOfGrids[step['grid']-1].grid[step['x']][step['y']]
                    if self.policy.arrayOfGrids[step['grid']-1].grid[step['x']][step['y']] != bestAction:
                         self.policy.arrayOfGrids[step['grid']-1].grid[step['x']][step['y']] = bestAction


     def printPolicyValue(self):
          print("***************************************POLICY****************************************\n{}\n***************************************POLICY****************************************\n".format(self.policy.printOutPolicy())) if debug else False #debug
          for i in range(len(self.StateAction)):
               print("STATEACTION: {}".format(i))
               print("\n***************************************StateAction****************************************\n{}\n***************************************StateAction****************************************".format(self.StateAction[i].printOut())) #debug
               print("\n***************************************StateActionTimesPICKED****************************************\n{}\n***************************************StateAction****************************************".format(self.StateActionTimesVisted[i].printOut())) #debug

          print("POLICY: Grid World Printout: {}".format(self.policy.arrayOfGrids)) if debug else False
          print("VALUE: Grid World Printout: {}".format(self.StateAction)) if debug else False

