class gridWorld:

    def __init__(self, length, width):
        self.board = [None] * length
        self.length = length
        self.width = width
        for i in range(length):
            self.board[i] = [None] * width
            #self.board = [[None]*4,[None]*4,[None]*4, [None]*4]

    def __str__(self):
        for row in self.board:
            print(row)
        return ""

    '''
    def printBoard(self, agent):
        for l in range(self.length):
            for w in range(self.width):
                if (l==agent.y and w == agent.x):
                    print("agent", end=",")
                else:
                    print(self.board[l][w], end=',')
            print("")
    '''
    def fill(self):
        count = 1
        for l in range(self.length):
            for w in range(self.width):
                if( (l==0 and w == 0) or (l==self.length-1 and w==self.width-1) ):
                    self.board[l][w] = 0
                else:
                    self.board[l][w] = count
                    count += 1