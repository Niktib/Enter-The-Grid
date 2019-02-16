debug = True

class agent:

    def __init__(self, name, board):
        self.name = name
        self.board = board
        self.x = board.length / 2
        self.y = board.width / 2
        self.totalReward = 0
        self.position = (self.x,self.y)
    
    def moveUp(self):  
        if (self.y > 0):
             self.y += -1
        else:
            print("invalid") if debug else None #debug
    
    def moveDown(self):
        if (self.y < self.board.length):
            self.y += +1
        else:
            print("invalid") if debug else None #debug
            
    
    def moveLeft(self):
        if (self.x > 0):
            self.x += -1
        else:
            print("invalid") if debug else None #debug

    def moveRight(self):
        if (self.x < self.board.width):
            self.x += +1
        else:
            print("invalid") if debug else None #debug