from boardAI import Board

TIME = 0
class GameController:
    def __init__(self, form, size, ai1, ai2):
        self.board = Board(size)
        self.board.set(3, 3, True)
        self.board.set(4, 4, True)
        self.board.set(3, 4, False)
        self.board.set(4, 3, False)
        self.size = size
        self.ai1 = ai1
        self.ai2 = ai2
        self.form = form
        self.previousMove = None
        self.is_end = False

    def play(self):
        while not self.board.is_end:
            self.previousMove = self.ai1.nextHand(self.board, self.previousMove, True)
            self.board.set(self.previousMove.row, self.previousMove.column, True)

            self.board.end_check()

            self.previousMove = self.ai2.nextHand(self.board, self.previousMove, False)
            self.board.set(self.previousMove.row, self.previousMove.column, False)

            self.board.end_check()
        

        print("black : "+str(self.board.getPieceNum(True))) 
        print("white : "+str(self.board.getPieceNum(False))) 
        
         