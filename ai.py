from board import Board
from place import Place


class BasicAI:
    def nextHand(self, board, previouseMove, isBlack):
        for i in range(board.size):
            for j in range(board.size):
                if board.canPlace(i, j, isBlack):
                    return Place(i, j)
