import PuzzleGame
from tkinter import *


def main():
    """
    main function, which create a tkinter object,
    and start the game
    """
    root = Tk()
    PuzzleGame.PuzzleGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
