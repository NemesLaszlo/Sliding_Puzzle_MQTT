import os
from tkinter import *
from tkinter import filedialog
import Board


class PuzzleGame:

    def __init__(self, parent):
        self.parent = parent
        self.image = StringVar()
        self.grid = IntVar()
        self.win_text = StringVar()

        self.mainFrame = Frame(self.parent)
        self.board = Frame(self.parent)
        self.winFrame = Frame(self.parent)
        self.create_startmenu()

    def create_startmenu(self):
        Label(self.mainFrame, text="MQTT Sliding Puzzle", font=("", 50)).pack(padx=10, pady=10)
        frame = Frame(self.mainFrame)
        Label(frame, text="Image").grid(sticky=W)
        Entry(frame, textvariable=self.image, width=50).grid(row=0, column=1, padx=10, pady=10)
        Button(frame, text="Browse", command=self.browse_image).grid(row=0, column=2, padx=10, pady=10)
        Label(frame, text="Grid").grid(sticky=W)
        OptionMenu(frame, self.grid, *[2, 3, 4, 5, 6, 7, 8, 9, 10]).grid(row=1, column=1, padx=10, pady=10, sticky=W)
        frame.pack(padx=10, pady=10)
        Button(self.mainFrame, text="Start", command=self.start).pack(padx=10, pady=10)
        self.mainFrame.pack()
        Label(self.winFrame, textvariable=self.win_text, font=("", 50)).pack(padx=10, pady=10)
        Button(self.winFrame, text="Play Again", command=self.play_again).pack(padx=10, pady=10)

    def start(self):
        image = self.image.get()
        grid = self.grid.get()
        if os.path.exists(image):
            self.board = Board.Board(parent=self.parent, image=image, grid=grid, win=self.win)
            self.mainFrame.pack_forget()
            self.board.pack()

    def browse_image(self):
        self.image.set(filedialog.askopenfilename(
            title="Select Image",
            filetype=(("png File", "*.png"), ("jpg File", "*.jpg"))))

    def win(self, moves):
        self.board.pack_forget()
        self.win_text.set("You are win, with {0} moves.".format(moves))
        self.winFrame.pack()

    def play_again(self):
        self.winFrame.pack_forget()
        self.mainFrame.pack()
