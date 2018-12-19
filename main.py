import tkinter as tk
from controller import GameController
from ai import BasicAI


class Frame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.form = MainForm(self)


class MainForm(tk.Canvas):
    size = 8
    cell_size = 60
    margin = 7

    def __init__(self, master):
        width = self.size*self.cell_size + 1
        tk.Canvas.__init__(self, master, relief=tk.RAISED, bd=4, bg="green", width=width, height=width)

        self.grid(column=0, row=0)

        self.controller = GameController(self, self.size, BasicAI(), BasicAI())
        self.controller.play()

    def refresh(self, board):
        for i in range(self.size):
            for j in range(self.size):
                x0 = i * self.cell_size + self.margin
                y0 = j * self.cell_size + self.margin
                self.create_rectangle(x0, y0, x0+self.cell_size, y0+self.cell_size, fill="green")
                if not board.isBlank(j, i) and board.isBlack(j, i):
                    self.create_oval(x0+2, y0+2, x0+self.cell_size-2, y0+self.cell_size-2, fill="black")
                elif not board.isBlank(j, i) and not board.isBlack(j, i):
                    self.create_oval(x0+2, y0+2, x0+self.cell_size-2, y0+self.cell_size-2, fill="white")
    
    def refresh_color(self, board, isBlack):
        self.refresh(board)
        for i in range(self.size):
            for j in range(self.size):
                if board.canPlace(j, i, isBlack):
                    x = i * self.cell_size + self.margin + self.cell_size/2
                    y = j * self.cell_size + self.margin + self.cell_size/2
                    self.create_text(x, y, text=str(board.getEValue(j, i, isBlack)), justify="center")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("othello")
    root.geometry("500x500")
    frame = Frame(master=root)
    frame.mainloop()
