from tkinter import Tk, BOTH, Canvas
import time

class Window:
    def __init__(self, width, height):
        self.width = width 
        self.height = height
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.root.title("Main Tkinter Window")
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()
        self.window_running = False
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.window_running = True
        while self.window_running == True:
            self.redraw()

    def close(self):
        self.window_running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_1, point_2):
        self.p1 = point_1
        self.p2 = point_2
    
    def draw(self, canvas, fill_color):
        x1 = self.p1.x
        y1 = self.p1.y
        x2 = self.p2.x
        y2 = self.p2.y

        canvas.create_line(
            x1, y1, x2, y2, fill=fill_color, width=2
        )


class Cell:
    def __init__(self, point_1, point_2, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = point_1.x
        self._x2 = point_2.x
        self._y1 = point_1.y
        self._y2 = point_2.y
        self._win = win
        CELL_SIZE = 50

    def draw(self):
        if self.has_left_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line, "black")

        if self.has_right_wall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(line, "black")

        if self.has_top_wall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line, "black")

        if self.has_bottom_wall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line, "black")
    
    def draw_move(self, to_cell, undo=False):
        val_cell_one_x = (self._x1 + self._x2) / 2
        val_cell_one_y = (self._y1 + self._y2) / 2
        val_cell_two_x = (to_cell._x1 + to_cell._x2) / 2
        val_cell_two_y = (to_cell._y1 + to_cell._y2) / 2
        line = Line(Point(val_cell_one_x, val_cell_one_y), Point(val_cell_two_x, val_cell_two_y))
        
        if undo:
            self._win.draw_line(line, "gray")
        else:
            self._win.draw_line(line, "red")

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
    # First create all cells
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                x1 = self.x1 + (j * self.cell_size_x)
                y1 = self.y1 + (i * self.cell_size_y)
                x2 = self.x1 + ((j + 1) * self.cell_size_x)
                y2 = self.y1 + ((i + 1) * self.cell_size_y)
                new_cell = Cell(Point(x1, y1), Point(x2, y2), self.win)
                row.append(new_cell)
            self._cells.append(row)

        # Then draw all cells
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        cell.draw()
        self._animate()


    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)


