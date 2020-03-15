import random
from tkinter import *


class Tiles:

    def __init__(self, grid):
        self.tiles = []
        self.grid = grid
        self.gap = None
        self.moves = 0

    def add(self, tile):
        self.tiles.append(tile)

    def get_tile(self, *pos):
        for tile in self.tiles:
            if tile.pos == pos:
                return tile

    def get_tile_around_gap(self):
        g_row, g_col = self.gap.pos
        return self.get_tile(g_row, g_col - 1), \
               self.get_tile(g_row - 1, g_col), \
               self.get_tile(g_row, g_col + 1), \
               self.get_tile(g_row + 1, g_col)

    def change_gap(self, tile):
        try:
            g_pos = self.gap.pos
            self.gap.pos = tile.pos
            tile.pos = g_pos
            self.moves += 1
        except:
            pass

    def slide(self, key):
        left, top, right, down = self.get_tile_around_gap()
        if key == "Up":
            self.change_gap(down)
        if key == "Down":
            self.change_gap(top)
        if key == "Left":
            self.change_gap(right)
        if key == "Right":
            self.change_gap(left)
        self.show()

    def suffle(self):
        random.shuffle(self.tiles)
        i = 0
        for row in range(self.grid):
            for col in range(self.grid):
                self.tiles[i].pos = (row, col)
                i += 1

    def show(self):
        for tile in self.tiles:
            if self.gap != tile:
                tile.show()

    # res, avagy ures kepkocka
    def set_gap(self, index):
        self.gap = self.tiles[index]

    def is_correct(self):
        for tile in self.tiles:
            if not tile.is_correct_pos():
                return False
        return True


class Tile(Label):

    def __init__(self, parent, image, pos):
        Label.__init__(self, parent, image=image)
        self.image = image
        self.pos = pos
        self.curr_pos = pos

    def show(self):
        self.grid(row=self.pos[0], column=self.pos[1])

    def is_correct_pos(self):
        return self.pos == self.curr_pos
