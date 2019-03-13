import GridWorld
import gridAgent
import random
import plotgrid

debug = True
class testbed:

    def __init__(self, randomSpwan=False):
        start={"grid": 1, "x" : 2 , "y" : 2}
        goal={"grid": 3, "x" : 4 , "y" : 0}
        self.gridWorld = GridWorld.GridWorld(start=start,goal=goal)
        if randomSpwan:
            agent = gridAgent.Agent(self.gridWorld,None)
        else:
            agent = gridAgent.Agent(self.gridWorld,None)

        self.gridWorld.pieceItTogether()
        #self.plotgrid = plotgrid.plotReward("DunRun Reward Plot")
        self.episodeList = plotgrid.plotReward("Episode Graph")

    def run(self, iterations, episodes):
        bestReward = -iterations
        bestIteration = 1
        numOfEpisodes = 0
        goalsFound = 0
        for iter in range(1, iterations+1):
            self.gridWorld.resetGrid()
            for ep in range(1,episodes+1):
                #self.plotgrid.LogResults(self.gridWorld.agent.reward)
                if self.gridWorld.agent.Done:
                    goalsFound += 1
                    print("*******************Found Goal******************\nFinal Stats:\n{}\n{}\n***********************************************".format(self.gridWorld.agent.playerStatus(),self.gridWorld.agent.policy.printPolicyValue())) if debug else False
                    break
                self.gridWorld.printOut()
                self.gridWorld.agentMove()
                self.episodeList.LogResults(self.gridWorld.agent.stateActionArray[ep-1]['reward'])

                print("Iter: {}, Ep: {}, {}".format(iter, ep, self.gridWorld.agent.playerStatus())) if debug else False #debug
            self.gridWorld.agent.policy.updateStates(self.gridWorld.agent.stateActionArray)
            #self.plotgrid.plot()
            self.episodeList.plot()

            if self.gridWorld.agent.reward > bestReward:
                bestReward = self.gridWorld.agent.reward
                bestIteration = iter
                numOfEpisodes = len(self.gridWorld.agent.stateActionArray)
            self.gridWorld.agent.resetAgent(self.gridWorld.startPoint['x'],self.gridWorld.startPoint['y'],self.gridWorld.startPoint['grid'])
        print("BEST RUN: Reward: {} , Iteration: {}, numOfEpisodes: {}, goalsFound: {}".format(bestReward,bestIteration,numOfEpisodes, goalsFound))

test = testbed()
test.run(200, 1000)
