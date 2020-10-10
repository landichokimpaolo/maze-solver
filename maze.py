import sys
from time import sleep
from PIL import Image, ImageDraw, ImageFont

class Maze:
    def __init__(self):
        self.maze = []
        self.path = []
        self.frontier = []
        self.explored = []

        self.cols, self.rows = 0, 0
        self.start, self.finish = None, None

    def build(self):
        row = 0
        with open('mazes/maze2.txt', 'r') as file:
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
                row += 1
                self.rows = row
                self.cols = len(column)
                self.maze.append(column)

        return self.maze

    def visualize(self, label = False):
        bg, bs = 2, 75
        dimension = ((len(self.maze[0])) * (bs), (len(self.maze)) * (bs))
        colors = {'#': (30, 34, 30), 'A': (174, 23, 0), 'B': (46, 193, 22), '*': (218, 252, 102), ' ': (255, 255, 255)}

        img = Image.new('RGB', dimension)
        drw = ImageDraw.Draw(img)

        for rk, rv in enumerate(self.maze):
            for ck, cv in enumerate(rv):
                pos = [ck * bs, rk * bs, (ck + 1) * bs, (rk + 1) * bs]
                drw.rectangle(pos, colors[cv], outline=(0, 0, 0), width=bg)

                if label:
                    font = ImageFont.truetype('assets/Lato-Bold.ttf', 14)
                    drw.text(((ck * bs) + 10, (rk * bs) + 10), f'{rk}, {ck}', font=font, fill=(189, 195, 199))
        img.show()

    def neighbors(self, target):
        row, col = target
        neighbors = []

        if col > 0:
            if self.maze[row][col - 1] in [' ', 'B']:
                neighbors.append((row, col - 1))
        if row + 1 < self.rows:
            if self.maze[row + 1][col] in [' ', 'B']:
                neighbors.append((row + 1, col))
        if col + 1 < self.cols:
            if self.maze[row][col + 1] in [' ', 'B']:
                neighbors.append((row, col + 1))
        if row > 0:
            if self.maze[row - 1][col] in [' ', 'B']:
                neighbors.append((row - 1, col))

        return neighbors

    def solve(self):
        self.frontier = self.neighbors(self.start)

        while len(self.frontier) != 0:
            row, col = self.frontier[-1]
            if self.maze[row][col] == 'B':
                break
            self.maze[row][col] = '*'
            self.frontier.pop()
            self.frontier += filter(lambda n: n not in self.frontier, self.neighbors((row, col)))

if __name__ == '__main__':
    maze = Maze()

    maze.build()
    maze.solve()
    maze.visualize(label=False)