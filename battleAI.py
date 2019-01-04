from controllerAI import GameController
from simpleAI import BasicAI

class Battle():
    
    def __init__(self):
        self.size = 8 
        self.controller = GameController(self, self.size, BasicAI(), BasicAI(is_random=True))

    def start(self):
        self.controller.play()

if __name__ == "__main__":
    game = Battle()
    game.start()
    game.controller.board.icon()

    
        