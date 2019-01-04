from boardAI import Board
import copy

class State(Board):
    def __init__(self, previousIsBlack,board=None, state=None,  previousMove=None):
        super().__init__(size=8)
        self.previousMove = previousMove
        self.previousIsBlack = previousIsBlack 
        self.eValue = 0
        self.previousState = state
        self.nextStateList = []
        if state:
            self.cells = copy.deepcopy(state.cells)
            self.set(previousMove.row, previousMove.column, previousIsBlack)
        else:
            self.cells = copy.deepcopy(board.cells)

    
    def copyEValueOnCanPlace(self, board, isBlack):
        for i in range(board.size):
            for j in range(board.size):
                if self.canPlace(i, j, isBlack):
                    board.setEValue(i,j, isBlack, self.getEValue(i,j,isBlack))

    def sortNextStateList(self, isMax, nth):
        valueList = []
        nextState = None
        for state in self.nextStateList:
            valueList.append(state.eValue)

        valueList.sort()
        if not isMax:
            valueList.reverse()
            
        for i in range(len(valueList)):
            if valueList[0] == self.nextStateList[i].eValue:
                nextState = self.nextStateList[i]
        
        return nextState
