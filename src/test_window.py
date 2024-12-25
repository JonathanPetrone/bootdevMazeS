import unittest
from window import *

class TestWindow(unittest.TestCase):
    def test_window_initialization(self):
        win = Window(800, 600)
        
        self.assertEqual(win.width, 800, "Width should be 800")
        self.assertEqual(win.height, 600, "Height should be 600")
        self.assertEqual(win.root.title(), "Main Tkinter Window", "Title should be 'Main Tkinter Window'")
        self.assertEqual(win.canvas.cget("width"), "800", "Canvas width should be 800")
        self.assertEqual(win.canvas.cget("height"), "600", "Canvas height should be 600")
        self.assertFalse(win.window_running, "Window running state should initially be False")

class TestMaze(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows, 
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols, 
        )
    
    def test_break_entrance_and_exit(self):
        maze = Maze(0, 0, 2, 2, 10, 10, None)
        
        maze._break_entrance_and_exit()
        
        entrance_cell = maze._cells[0][0]
        exit_cell = maze._cells[-1][-1]
        
        self.assertFalse(entrance_cell.has_top_wall)
        self.assertFalse(exit_cell.has_bottom_wall)


if __name__ == '__main__':
    unittest.main()