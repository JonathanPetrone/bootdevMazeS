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

if __name__ == '__main__':
    unittest.main()