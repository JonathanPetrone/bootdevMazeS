from tkinter import Tk, BOTH, Canvas
import time
import random

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
    
    def wait_for_close(self):
        self.window_running = True
        self._check_window_state()

    def _check_window_state(self):
        if self.window_running:
            self.redraw()
            self.root.after(100, self._check_window_state)  # Check the window state every 100ms to prevent freezing

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
    def __init__(self, point_1, point_2, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = point_1.x
        self._x2 = point_2.x
        self._y1 = point_1.y
        self._y2 = point_2.y
        self._win = win
        self.visited = False
        CELL_SIZE = 50

    def draw(self):
        if self._win is not None:
            if self.has_left_wall:
                line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
                self._win.draw_line(line, "black")
            else:
                line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
                self._win.draw_line(line, "#d9d9d9")

            if self.has_right_wall:
                line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
                self._win.draw_line(line, "black")
            else:
                line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
                self._win.draw_line(line, "#d9d9d9")

            if self.has_top_wall:
                line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
                self._win.draw_line(line, "black")
            else:
                line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
                self._win.draw_line(line, "#d9d9d9")

            if self.has_bottom_wall:
                line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
                self._win.draw_line(line, "black")
            else:
                line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
                self._win.draw_line(line, "#d9d9d9")
    
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
        win=None,
        margin=10  # Set margin to 10 as default
    ):
        self.margin = margin
        self.x1 = x1 + self.margin
        self.y1 = y1 + self.margin
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
        if self.win is not None:
            cell = self._cells[i][j]
            cell.draw()
            self._animate()


    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]  # Notice we use _grid to get the actual cell
        exit_cell = self._cells[-1][-1]

        entrance_cell.has_top_wall = False
        entrance_cell.draw()  # Directly call draw on the cell

        exit_cell.has_bottom_wall = False
        exit_cell.draw()  
    
    def _break_walls_r(self, i, j):
        current = self._cells[i][j]
        current.visited = True

        directions = {
            "UP": (-1, 0),
            "DOWN": (1, 0),
            "LEFT": (0, -1),
            "RIGHT": (0, 1)
        }

        while True:
            list_cells = []
            # For cell above
            if (i-1) >= 0 and (i-1) < self.num_rows and j >= 0 and j < self.num_cols:
                if (i-1) >= 0 and not self._cells[i-1][j].visited:
                    list_cells.append(((i-1, j), "UP"))
            # For cell below
            if (i+1) >= 0 and (i+1) < self.num_rows and j >= 0 and j < self.num_cols:
                if not self._cells[i+1][j].visited:
                    list_cells.append(((i+1, j), "DOWN"))
            # For left cell
            if (i >= 0 and i < self.num_rows and (j-1) >= 0 and (j-1) < self.num_cols):
                if not self._cells[i][j-1].visited:
                    list_cells.append(((i, j-1), "LEFT"))
            # For right cell
            if (i >= 0 and i < self.num_rows and (j+1) >= 0 and (j+1) < self.num_cols):
                if not self._cells[i][j+1].visited:
                    list_cells.append(((i, j+1), "RIGHT"))
            
            # Check for possible moves
            if list_cells:
                # Randomly select a cell and direction
                (new_i, new_j), direction = random.choice(list_cells)
                
                # Use direction to knock down walls
                if direction == "UP":
                    # Modify walls for UP...
                    current.has_top_wall = False
                    # Knock down the bottom wall of the cell above
                    self._cells[new_i][new_j].has_bottom_wall = False
                    self._break_walls_r(new_i, new_j)
                elif direction == "DOWN":
                    # Modify walls for DOWN...
                    current.has_bottom_wall = False
                    # Knock down the top wall of the cell below
                    self._cells[new_i][new_j].has_top_wall = False
                    self._break_walls_r(new_i, new_j)
                elif direction == "LEFT":
                    # Modify walls for LEFT...
                    current.has_left_wall = False
                    # Knock down the right wall of the cell to the left
                    self._cells[new_i][new_j].has_right_wall = False
                    self._break_walls_r(new_i, new_j)
                elif direction == "RIGHT":
                    # Modify walls for RIGHT...
                    current.has_right_wall = False
                    # Knock down the left wall of the cell to the right
                    self._cells[new_i][new_j].has_left_wall = False
                    self._break_walls_r(new_i, new_j)
            else:
                return
            
    def draw_maze(self):
        # Draw entrance and exit
        self._break_entrance_and_exit()

        # Break walls recursively and illustrate the process
        self._break_walls_r(0, 0)

        # Reset the visited status after breaking walls
        self._reset_cells_visited()

        # Draw the complete maze
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i, j)

    def _reset_cells_visited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._cells[i][j].visited = False
    
    def solve(self):
        solved = self._solve_r(0, 0)

        return solved
        
    
    def _solve_r(self, i, j):
        self._animate()
        current = self._cells[i][j]
        current.visited = True

        if i == self.num_rows - 1 and j == self.num_cols - 1:
            return True
        
        # For right movement: (j + 1) needs to be less than num_cols
        if j + 1 < self.num_cols:
            if not current.has_right_wall and not self._cells[i][j + 1].visited:
                current.draw_move(self._cells[i][j + 1])
                if self._solve_r(i, j + 1):
                    return True
                current.draw_move(self._cells[i][j + 1], True) 

        # For left movement: (j - 1) needs to be >= 0
        if j - 1 >= 0:
            if not current.has_left_wall and not self._cells[i][j - 1].visited:
                current.draw_move(self._cells[i][j - 1])
                if self._solve_r(i, j - 1):
                    return True
                current.draw_move(self._cells[i][j - 1], True)
        
        # For down movement: (i + 1) needs to be less than num_rows
        if i + 1 < self.num_rows:
            if not current.has_bottom_wall and not self._cells[i + 1][j].visited:  # fixed index
                current.draw_move(self._cells[i + 1][j])  # move down
                if self._solve_r(i + 1, j):  # recursive call down
                    return True
                current.draw_move(self._cells[i + 1][j], True)  # undo

        # For up movement: (i - 1) needs to be >= 0
        if i - 1 >= 0:
            if not current.has_top_wall and not self._cells[i - 1][j].visited:  # fixed index
                current.draw_move(self._cells[i - 1][j])  # move up
                if self._solve_r(i - 1, j):  # recursive call up
                    return True
                current.draw_move(self._cells[i - 1][j], True)  # undo
        
        return False


