from board import Board
import concurrent.futures
import time


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
        self.flag = True

    def play(self):
        self.isPlay = True
        self.form.refresh_color(self.board, True)
        
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
        executor.submit(self.turn)

    def turn_manual(self):
        if self.flag:
            self.previousMove = self.ai1.nextHand(self.board, self.previousMove, True)
            if self.previousMove is not None:
                self.board.set(self.previousMove.row, self.previousMove.column, True)
            self.flag = False
        else:
            self.previousMove = self.ai2.nextHand(self.board, self.previousMove, False)
            if self.previousMove is not None:
                self.board.set(self.previousMove.row, self.previousMove.column, False)
            self.flag = True
        self.form.refresh_color(self.board, self.flag)

    def turn(self):
        while self.isPlay:
            time.sleep(1)
            self.previousMove = self.ai1.nextHand(self.board, self.previousMove, True)
            if self.previousMove is not None:
                self.board.set(self.previousMove.row, self.previousMove.column, True)
            self.form.refresh_color(self.board, False)
            time.sleep(1)
            self.previousMove = self.ai2.nextHand(self.board, self.previousMove, False)
            if self.previousMove is not None:
                self.board.set(self.previousMove.row, self.previousMove.column, False)

            self.form.refresh_color(self.board, True)

    def end(self):
        self.isPlay = False

