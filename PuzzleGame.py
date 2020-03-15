import os
import platform
import random
from tkinter import *
import Board
import xml.dom.minidom


class PuzzleGame:

    def __init__(self, parent):
        self.parent = parent
        self.grid = 3
        self.send_config_xml_to_broker()
        self.board = Frame(self.parent)
        self.start()

    def send_config_xml_to_broker(self):
        xmlObject = xml.dom.minidom.parse("config_setup.xml")
        pretty_xml_as_string = xmlObject.toprettyxml()
        print(pretty_xml_as_string)

    def pick_random_picture(self):
        path_project = os.path.dirname(os.path.realpath(__file__))
        system = platform.system()
        if system == 'Linux' or system == 'Darwin':
            path_pictures = path_project + "/pictures"
            return str(path_pictures + "\\" + self.random_picture(path_pictures))
        elif system == 'Windows':
            path_pictures = path_project + "\\pictures"
            return str(path_pictures + "\\" + self.random_picture(path_pictures))

    def random_picture(self, place):
        random_filename = random.choice([
            x for x in os.listdir(place)
            if os.path.isfile(os.path.join(place, x))
        ])
        return random_filename

    def start(self):
        image = self.pick_random_picture()
        grid = self.grid
        if os.path.exists(image):
            self.board = Board.Board(parent=self.parent, image=image, grid=grid, win=self.win)
            self.board.pack()

    def win(self, moves):
        self.board.pack_forget()
        win_text = ("You are win, with {0} moves.".format(moves))
        print(win_text)
        self.play_again()

    def play_again(self):
        self.start()
