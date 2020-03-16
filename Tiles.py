import random
from tkinter import *


class Tiles:
    """
    Tiles object with the cropped picture parts -> tiles in list.
    """

    def __init__(self, grid):
        """
        Constructor of the Tiles.
        """
        self.tiles = []
        self.grid = grid
        self.gap = None
        self.moves = 0

    def add(self, tile):
        """
        tile - parameter, part of the picture.
        Add tile - picture element part to the list.
        """
        self.tiles.append(tile)

    def get_tile(self, *pos):
        """
        pos - position of tile.
        Get the actual tile, with this position parameter.
        Return this Tile object.
        """
        for tile in self.tiles:
            if tile.pos == pos:
                return tile

    def get_tile_around_gap(self):
        """
        Get the Tile object around the gap of the game.
        Return the "area" - with this tiles around the gap.
        """
        g_row, g_col = self.gap.pos
        return self.get_tile(g_row, g_col - 1), \
               self.get_tile(g_row - 1, g_col), \
               self.get_tile(g_row, g_col + 1), \
               self.get_tile(g_row + 1, g_col)

    def change_gap(self, tile):
        """
        Game movement in the game.
        """
        try:
            g_pos = self.gap.pos
            self.gap.pos = tile.pos
            tile.pos = g_pos
            self.moves += 1
        except:
            pass

    def slide(self, key):
        """
        Game coordination.
        """
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
        """
        Shuffle the picture parts - tiles. To play the game.
        """
        random.shuffle(self.tiles)
        i = 0
        for row in range(self.grid):
            for col in range(self.grid):
                self.tiles[i].pos = (row, col)
                i += 1

    def show(self):
        """
        Game visualization.
        """
        for tile in self.tiles:
            if self.gap != tile:
                tile.show()

    # res, avagy ures kepkocka
    def set_gap(self, index):
        """
        Set the gap, initialize on the board, to play the game.
        """
        self.gap = self.tiles[index]

    def is_correct(self):
        """
        Check the win period, the picture part - tile is in the good position or not.
        Return logical values.
        """
        for tile in self.tiles:
            if not tile.is_correct_pos():
                return False
        return True


class Tile(Label):
    """
    Tile object.
    Inherited from label.
    """

    def __init__(self, parent, image, pos):
        """
        Constructor of the Tile.
        """
        Label.__init__(self, parent, image=image)
        self.image = image
        self.pos = pos
        self.curr_pos = pos

    def show(self):
        """
        Game visualization. Tile visualize.
        """
        self.grid(row=self.pos[0], column=self.pos[1])

    def is_correct_pos(self):
        """
        Tile position check, fot the win check.
        """
        return self.pos == self.curr_pos
