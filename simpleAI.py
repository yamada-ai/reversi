from boardAI import Board
from place import Place
from stateAI import State
import random


class BasicAI:
    def __init__(self, is_random=False):
        self.depth = 1
        self.isInitialized = False
        self.closedList = []
        self.weightTable = self.setWeight()

        # 追加フィールド
        # ランダムにオセロするか否か
        self.is_random = is_random
    
    def setWeight(self):
        w = [
			[ 50,     -50,  6,  4,     4,   6, -50,  50],
			[-50,    -50,   4,  2,    2,  4, -50, -50],
			[ 6,        4,     6,  1,    1,  6,    4,   6],
			[ 4,        2,     1,   0,   0 , 1,    2,   4],
			[ 4 ,       2,     1,   0,   0,  1,    2,   4],
			[ 6,       4,      6,   1,   1,  6,    4,   6],
			[-50,  -50,    4,    2,   2,  4, -50, -50],
			[  50,  -50,    6,   4,   4,  6, -50,  50]
			]
        return w
    
    def getWeight(self, row, column):
        return self.weightTable[row][column]

    

    def nextHand(self, board, previousMove, isBlack):
        if isBlack :
            if not board.canBlackPlace:
                return Place(-1, -1)
        else:
            if not board.canWhitePlace:
                return Place(-1, -1)

        if self.is_random:
            return self.randomNextHand(board, isBlack)


        return self.simpleBdSearchNextHand(board, previousMove, isBlack)

    
    def initializeEValue(self, board):
        if self.isInitialized:
            return
        else:
            for i in range(board.size):
                for j in range(board.size):
                    board.setEvalue(i, j, True, 0)
                    board.setEvalue(i, j, False, 0)
        self.isInitialized = True
    
    def incEValueOfAvailableMoves(self, board, isBlack):
        for i in range(board.size):
            for j in range(board.size):
                if board.canPlace(i, j, isBlack):
                    self.incEValue(board, i, j, isBlack)
                        
    
    def incEValue(self, board, row, column, isBlack):
        val = board.getEvalue(row, column, isBlack)
        board.setEvalue(row, column, isBlack, val+1)
    

    # 7.4
    def pieces(self, state, isBlack):
        return state.getPieceNum(isBlack)

    
    def canMoves(self, state, isBlack):
        num = 0
        for i in range(state.size):
            for j in range(state.size):
                if state.canPlace(i, j, isBlack):
                    num += 1
        return num
    
    def weightedPieces(self, state, isBlack):
        w = 0
        for i in range(state.size):
            for j in range(state.size):
                if not state.isBlank(i,j):
                    if state.isBlack(i,j) == isBlack:

                        w += self.getWeight(i,j)
        return w

    
    def canMoves2Pieces(self, state, isBlack):
        a = 20
        turn = self.pieces(state, True) + self.pieces(state, False) - 4
        if a >= turn:
            return self.canMoves(state, isBlack)
        return self.pieces(state, isBlack)
    

    def randomNextHand(self, board, isBlack):
        action = []
        for i in range(board.size):
            for j in range(board.size):
                if board.canPlace(i, j, isBlack):
                    action.append(Place(i,j))
        if len(action) == 0:
            print(isBlack)
            print(board.canWhitePlace)
            board.icon()
            board.calcCondition()
            print(board.canWhitePlace)
        return random.choice(action)
        


    
    def simpleBdSearchNextHand(self,board,previousMove, isBlack):
        previousIsBlack = not isBlack
        root = State(previousIsBlack, board=board, previousMove=previousMove)
        # root.icon()
        # board.icon()
        self.depth = 1

        nextState = None
        isMax = True
        nthPV = 1

        # 評価関数
        currentEf = self.weightedPieces
        rivalEf = self.weightedPieces

        nextState = self.simplebdSearch(root, isBlack, isMax, nthPV, currentEf, rivalEf)

        root.copyEValueOnCanPlace(board, isBlack)
        self.closedList.append(root)

        nextState.copyEValueOnCanPlace(board, previousIsBlack)
        self.closedList.append(nextState)

        return nextState.previousMove



    
    def simplebdSearch(self, root, isBlack, isMax, nthPV, currentEf, rivalEf):
        nth = nthPV - 1
        nextState = None
        self.expandNodeAndEvalThem(root, isBlack, currentEf)
        nextState = root.sortNextStateList(isMax, nth)

        self.expandNodeAndEvalThem(root, isBlack, rivalEf)

        return nextState

    
    def expandNodeAndEvalThem(self, state, isBlack, efunc):
        nextState = None
        # state.icon()
        for i in range(state.size):
            for j in range(state.size):
                if state.canPlace(i, j, isBlack):
                    move = Place(i, j)
                    nextState = self.lookAhead(state,move, isBlack, efunc)
                    state.nextStateList.append(nextState)
                    # print(nextState.eValue)
                    # state.nextStateList[nextState.eValue] = nextState
                    
    

    def lookAhead(self, state, move, isBlack, efunc):
        nextState = State(isBlack, state=state, previousMove=move)
        eValue = efunc(nextState, isBlack)
        nextState.eValue = eValue

        state.setEValue(move.row, move.column, isBlack, eValue)
        

        return nextState
