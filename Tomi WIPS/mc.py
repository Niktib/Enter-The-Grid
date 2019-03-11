import random
import GridWorld
class monteCarlo:
     
     def __init__(self, valueState, policyState):
          self.value = valueState
          self.policy = policyState
          self.initPolicy()
          self.printPolicyValue()
          

     def decision(self,state):
          move = self.policy.arrayOfGrids[state['grid']-1].grid[state['x']][state['y']]
          print("Decision: {}".format(move))
          return move
          
     def onPolicyEsoft(self, epislon=0.1):
          pass

     def initPolicy(self):
          for grid in self.policy.arrayOfGrids:
               #initalize random policy
               for i in range(len(grid.grid)):
                    for j in range(len(grid.grid[i])):
                        grid.grid[i][j] = random.randint(1,4)
     
     def printPolicyValue(self):
          print("***************************************POLICY****************************************\n{}\n***************************************POLICY****************************************\n\n***************************************VALUE****************************************\n{}\n***************************************VALUE****************************************".format(self.policy.printOut(),self.value.printOut()))
          print("POLICY: Grid World Printout: {}".format(self.policy.arrayOfGrids))	
          print("VALUE: Grid World Printout: {}".format(self.value.arrayOfGrids))

