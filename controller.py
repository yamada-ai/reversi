from board import Board
import concurrent.futures
import time

TIME = 0
# executor = None
class GameController:
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
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
        self.form.refresh_color(self.board, True)
        # executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
        self.executor.submit(self.turn)


    def end(self):
        print("end")
        self.executor.shutdown()
        

    def turn(self):
        global TIME
        q = 0
        while not self.is_end:
            print(q)
            time.sleep(TIME)
            self.previousMove = self.ai1.nextHand(self.board, self.previousMove, True)
            if self.previousMove is not None:
                self.board.set(self.previousMove.row, self.previousMove.column, True)
            self.form.refresh_color(self.board, False)
            time.sleep(TIME)
            self.previousMove = self.ai2.nextHand(self.board, self.previousMove, False)
            if self.previousMove is not None:
                self.board.set(self.previousMove.row, self.previousMove.column, False)

            self.form.refresh_color(self.board, True)
            q += 1
