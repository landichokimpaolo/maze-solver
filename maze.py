import sys
from PIL import Image, ImageDraw

class Maze:
    def __init__(self):
        self.maze = []
        self.start = None
        self.finish = None

    def build(self):
        row = 0
        with open('maze2.txt', 'r') as file:
            column = []
            for char in file.read():
                if char == 'A':
                    self.start = (row, len(column))
                if char == 'B':
                    self.finish = (row, len(column))

                if char != '\n':
                    column.append(char)
                else:
                    self.maze.append(column)
                    column = []
                    row += 1
            else:
                self.maze.append(column)
                row += 1

        return self.maze

    def visualize(self):
        bg, bs = 2, 75
        dimension = ((len(self.maze[0])) * (bs), (len(self.maze)) * (bs))
        colors = {'#': (30, 34, 30), 'A': (174, 23, 0), 'B': (46, 193, 22), '*': (218, 252, 102), ' ': (255, 255, 255)}

        img = Image.new('RGB', dimension)
        drw = ImageDraw.Draw(img)

        for rk, rv in enumerate(self.maze):
            for ck, cv in enumerate(rv):
                pos = [ck * bs, rk * bs, (ck + 1) * bs, (rk + 1) * bs]
                drw.rectangle(pos, colors[cv], outline=(0, 0, 0), width=bg)
        img.show()

maze = Maze()
maze.build()
maze.visualize()