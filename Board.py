from tkinter import *
from PIL import Image, ImageTk
import Tiles

MAX_BOARD_SIZE = 500


class Board(Frame):

    def __init__(self, parent, image, grid, win,  *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent
        self.grid = grid
        self.win = win
        self.image = self.open_image(image)
        self.tile_size = self.image.size[0] / self.grid
        self.tiles = self.create_tiles()
        self.tiles.suffle()
        self.tiles.show()
        self.bind_keys()

    def open_image(self, image):
        image = Image.open(image)
        if min(image.size) > MAX_BOARD_SIZE:
            image = image.resize((MAX_BOARD_SIZE, MAX_BOARD_SIZE), Image.ANTIALIAS)
        if image.size[0] != image.size[1]:
            image = image.crop((0, 0, image.size[0], image.size[0]))
        return image

    def create_tiles(self):
        tiles = Tiles.Tiles(grid=self.grid)

        for row in range(self.grid):
            for col in range(self.grid):
                x0 = col * self.tile_size
                y0 = row * self.tile_size
                x1 = x0 + self.tile_size
                y1 = y0 + self.tile_size
                tile_image = ImageTk.PhotoImage(self.image.crop((x0, y0, x1, y1)))
                tile = Tiles.Tile(self, tile_image, (row, col))
                tiles.add(tile)
        tiles.set_gap(-1)
        return tiles

    def bind_keys(self):
        self.bind_all("<Key-Up>", self.slide)
        self.bind_all("<Key-Down>", self.slide)
        self.bind_all("<Key-Right>", self.slide)
        self.bind_all("<Key-Left>", self.slide)

    def slide(self, event):
        self.tiles.slide(event.keysym)
        if self.tiles.is_correct():
            self.win(self.tiles.moves)

