import matplotlib.pyplot as plt

class plotReward:
    def __init__(self,name):
        self.name = name
        self.rewardList = list()
        self.Epcount = list()
        self.ProbGraph = plt

    def LogResults(self,AverageReward, Episode):
        self.rewardList.append(AverageReward)
        self.Epcount = Episode
        pass
        
    def LogProb(self, Probability):
        self.ProbGraph.plot(Probability, label='Chance of Picking Optimal Arm')

    def plotProb(self, WhichAlgorithm):
        if (WhichAlgorithm == 1): self.name = "UCB"
        elif (WhichAlgorithm == 2): self.name = "LRI"
        elif (WhichAlgorithm == 3): self.name = "LRP"
        #plt.plot(self.rewardList,label='Chance of Picking Optimal Arm')
        self.ProbGraph.xlabel('Steps')
        self.ProbGraph.ylabel('Probability')
        self.ProbGraph.title('Probability over 20 Runs')
        self.ProbGraph.grid(True)
        self.ProbGraph.savefig('GraphOf{}.png'.format(self.name))
        self.ProbGraph.clf() #clear the current graph, can be removed to see all values on one chart

    def plot(self):
        plt.bar(self.Epcount, self.rewardList,label=self.name)
        plt.xlabel('Episode')
        plt.ylabel('Number Of Steps')
        plt.title('Episode to Steps for {}'.format(self.name))
        plt.grid(True)
        plt.savefig('GraphOf{}.png'.format(self.name))
        self.rewardList = []
        #plt.clf() #clear the current graph, can be removed to see all values on one chart